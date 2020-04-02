import schedule
from settings import config
from move_reports import Reports

# O
o_reports = Reports(config['o']['source'], config['o']['destination'])
# Z
z_reports = Reports(config['z']['source'], config['z']['destination'])
# R
r_reports = Reports(config['r']['source'], config['r']['destination'])

# Schedule
schedule.every(10).minutes.do(o_reports.move)
schedule.every().day.at('05:00').do(r_reports.move_period)
schedule.every().day.at('06:00').do(z_reports.move_or_copy)
schedule.every().day.at('08:00').do(z_reports.move_or_copy)
schedule.every().day.at('12:00').do(z_reports.move_or_copy)
schedule.every().day.at('14:00').do(z_reports.move_or_copy)
schedule.every().day.at('16:00').do(z_reports.move_or_copy)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
