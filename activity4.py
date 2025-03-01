import datetime

x=datetime.datetime.now()

print("Current time is",x)

print("Current hour is",x.strftime ("%H"))

print("Current minutes is",x.strftime ("%M"))

print("Current seconds is",x.strftime ("%S"))

print("Today is",x.strftime ("%A"))

print("This is",x.strftime ("%B"))

import calendar

print(calendar.calendar(2025))

yy=2025
mm=8

print(calendar.month(yy,mm))