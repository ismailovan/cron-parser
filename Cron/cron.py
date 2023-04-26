class Cron:
    def __init__(self, cron_str: str):
        minute_f, hour_f, day_f, month_f, day_w_f, command = cron_str.split()

        self.minute = Cron.range_val(minute_f, 0, 59)
        self.hour   = Cron.range_val(hour_f,   0, 23)
        self.day    = Cron.range_val(day_f,    1, 31)
        self.month  = Cron.range_val(month_f,  1, 12)
        self.day_w  = Cron.range_val(day_w_f,  1, 7 )
        self.command = command
    
    @staticmethod
    def range_val(field: str, min_v: int, max_v: int, step: int = 0) -> list:
        # split by comma
        if ',' in field:
            time_stamps = field.split(',')
            # for each substring separated by comma recursively get range_val
            # then join them together, delete repetitions and sort
            return sorted(list(set(item for t in time_stamps for item in Cron.range_val(t, min_v, max_v))))
        # get step value
        elif '/' in field:
            left, step = field.split('/')
            step = int(step)
            # recursively get range_val with specified step
            return Cron.range_val(left, min_v, max_v, step)
    
        # either '-' or '*' or one number is present
        elif '-' in field:
            start, end = map(int, field.split('-'))
            # range is specified
            return list(range(start, end + 1, step + (step == 0)))
        elif '*' in field:
            # range is not specified
            return list(range(min_v, max_v + 1, step + (step == 0)))
        # check the number
        elif step != 0:
            # if number is specified with step then it is range
            return list(range(int(field), max_v + 1, step))
        else:
            # otherwise it is one single number
            return [int(field)]
