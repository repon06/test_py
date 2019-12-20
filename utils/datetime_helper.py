import datetime
import time
from datetime import datetime


def get_date(date_time):
    ''' 1966-07-10 00:00:00 '''
    #date_object = time.strptime('1966-07-10 00:00:00', '%Y-%m-%d %H:%M:%S')
    date_object = time.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    # print(date_object)
    date = time.strftime('%d.%m.%Y', date_object)
    # print(date)
    return date
