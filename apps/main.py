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
schedule.every(30).minutes.do(z_reports.move_or_copy)
schedule.every().day.at('03:00').do(r_reports.move_period)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
