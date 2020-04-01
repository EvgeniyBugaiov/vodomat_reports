import os
import datetime
from shutil import move, copyfile


class Reports:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    @staticmethod
    def date_created(file):
        return datetime.date.fromtimestamp(os.stat(file).st_mtime)
    
    def move(self):
        for path, _, files in os.walk(self.source):
            for file in files:
                if file.endswith('.xml'):
                    move(os.path.join(path, file), self.destination)
    
    def move_period(self, end_perion=datetime.date.today()):
        for path, _, files in os.walk(self.source):
            for file in files:
                if file.endswith('.xml'):
                    file_date_created = self.date_created(os.path.join(path, file))
                    if file_date_created < end_perion:
                        move(os.path.join(path, file), os.path.join(self.destination, file))

    def move_or_copy(self):
        for path, _, files in os.walk(self.source):
            for file in files:
                if file.endswith('.xml'):
                    file_date_created = self.date_created(os.path.join(path, file))
                    if file_date_created < datetime.date.today():
                        move(os.path.join(path, file), os.path.join(self.destination, file))
                    else:
                        copyfile(os.path.join(path, file), os.path.join(self.destination, file))
