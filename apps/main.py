import schedule
from settings import config
from reports import Reports

# O
o_reports = Reports(config['o']['source'], config['o']['destination'], config['archive'])
# Z
z_reports = Reports(config['z']['source'], config['z']['destination'], config['archive'])
# R
r_reports = Reports(config['r']['source'], config['r']['destination'], config['archive'])
# X
x_reports = Reports(config['x']['source'])

# Schedule
schedule.every(10).minutes.do(o_reports.move_all)
# --------------------------------------------------------
schedule.every().day.at('03:00').do(o_reports.create_week_archive)
schedule.every().day.at('03:10').do(z_reports.create_week_archive)
schedule.every().day.at('03:20').do(r_reports.create_week_archive)
# --------------------------------------------------------
schedule.every().day.at('05:00').do(r_reports.move_period)
# --------------------------------------------------------
schedule.every().day.at('06:00').do(z_reports.move_or_copy)
schedule.every().day.at('08:00').do(z_reports.move_or_copy)
schedule.every().day.at('11:00').do(z_reports.move_or_copy)
schedule.every().day.at('12:00').do(z_reports.move_or_copy)
schedule.every().day.at('14:00').do(z_reports.move_or_copy)
schedule.every().day.at('16:00').do(z_reports.move_or_copy)
# --------------------------------------------------------
schedule.every().day.at('10:10').do(x_reports.delete_period)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
