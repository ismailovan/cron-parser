import sys
from cron import Cron

def parser(cron_str: str):
    range_val = Cron.range_val
    minute_f, hour_f, day_f, month_f, day_w_f, command = cron_str.split()

    minute = range_val(minute_f, 0, 59)
    hour   = range_val(hour_f,   0, 23)
    day    = range_val(day_f,    1, 31)
    month  = range_val(month_f,  1, 12)
    day_w  = range_val(day_w_f,  1, 7 )

    print('minute',       ' '.join(map(str, minute)))
    print('hour',         ' '.join(map(str, hour)))
    print('day of month', ' '.join(map(str, day)))
    print('month',        ' '.join(map(str, month)))
    print('day of week',  ' '.join(map(str, day_w)))
    print('command', command)

if __name__ == '__main__':
    cron_str = sys.argv[1]
    parser(cron_str)
    
    
