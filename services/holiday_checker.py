import datetime
import holidays

def is_holiday(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
    indo_holidays = holidays.Indonesia(years=date_obj.year)
    return date_obj.weekday() == 6 or date_obj in indo_holidays
