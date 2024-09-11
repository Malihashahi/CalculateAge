import time
from calendar import isleap


def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

def to_hours(days):
    hours=days*24
    return hours

def to_seconds(days):
    sec=days*24*3600
    return sec




age = input("input your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year


for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
hours=to_hours(day)
seconds=to_seconds(day)
print("age is %d years or " % ( year), end="")
print("%d months or %d days" % (month, day),end="")
print(" or %d hours or %d seconds" % (hours,seconds))