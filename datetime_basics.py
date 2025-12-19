# datetime module
#   Functions that handle time, date, time intervals
#   Dates are objects not strings
#   Can print output as date/time structure or provide present time
#   Year > Month > Day > Hour > Minute > Second > Microsecond

import datetime

print("\nThe current full time is {}".format(datetime.datetime.now()))
h = datetime.datetime.now().hour
m = datetime.datetime.now().minute
s = datetime.datetime.now().second
print("\nThe current time is {}:{}:{}".format(h,m,s))

print("Current time: {}".format(datetime.time(5,58)))
print("Current date: {}".format(datetime.date(2023,9,23)))
