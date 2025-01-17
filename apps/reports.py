import os
import datetime
import shutil
from zipfile import ZipFile


class Reports:
    def __init__(self, source, destination='', archive=''):
        self.source = source
        self.destination = destination
        self.archive = os.path.join(destination, archive)
    
    def __repr__(self):
        return f'Reports(Source: "{self.source}", Destination: "{self.destination}", Archive: "{self.archive}")'
    
    @staticmethod
    def date_created(file):
        return datetime.date.fromtimestamp(os.stat(file).st_mtime)

    def create_week_archive(self):
        for path, _, files in os.walk(self.archive):
            for file in files:
                if file.endswith('.xml'):
                    file_path = os.path.join(path, file)
                    file_date_created = self.date_created(file_path)
                    zip_file = '{year}-{month} ({week}).zip'.format(year=file_date_created.year,
                                                                    month=file_date_created.month,
                                                                    week=file_date_created.isocalendar()[1])
                    zip_file_path = os.path.join(self.archive, zip_file)
                    if os.path.exists(zip_file_path):
                        with ZipFile(zip_file_path, 'a') as week_archive:
                            week_archive.write(file_path, file)
                    else:
                        with ZipFile(zip_file_path, 'w') as week_archive:
                            week_archive.write(file_path, file)
                    os.remove(file_path)
    
    def move_all(self):
        for path, _, files in os.walk(self.source):
            for file in files:
                if file.endswith('.xml'):
                    try:
                        shutil.move(os.path.join(path, file), self.destination)
                    except shutil.Error:
                        continue
    
    def move_period(self, end_perion=datetime.date.today):
        for path, _, files in os.walk(self.source):
            for file in files:
                if file.endswith('.xml'):
                    file_date_created = self.date_created(os.path.join(path, file))
                    if file_date_created < end_perion():
                        shutil.move(os.path.join(path, file), os.path.join(self.destination, file))

    def move_or_copy(self, end_perion=datetime.date.today):
        for path, _, files in os.walk(self.source):
            for file in files:
                if file.endswith('.xml'):
                    file_date_created = self.date_created(os.path.join(path, file))
                    if file_date_created < end_perion():
                        shutil.move(os.path.join(path, file), os.path.join(self.destination, file))
                    else:
                        shutil.copyfile(os.path.join(path, file), os.path.join(self.destination, file))

    def delete_period(self, days=30):
        for path, _, files in os.walk(self.source):
            for file in files:
                if file.endswith('.xml'):
                    file_path = os.path.join(path, file)
                    file_date_created = self.date_created(file_path)
                    if file_date_created < datetime.date.today() - datetime.timedelta(days=days):
                        os.remove(file_path)
