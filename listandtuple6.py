import sys
#tuples are immutable lists

#example tuples
colours = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
data_structures = ('list', 'tuple', 'dictionary', 'object')
work_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
weekend_days = ('Saturday', 'Sunday')
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

weekdays = work_days + weekend_days
print(weekdays)
#sys.exit(0)

spring = months[2:5]
print(spring)
#sys.exit(0)

#tuples used to format strings
print("Spring months: %s, %s, %s" % ("March", "April", "May"))
print("Spring months: %s, %s, %s" % spring)
winter = (months[11], months[0], months[1])
print("Winter months: %s, %s, %s" % winter)
#sys.exit(0)

#packing
today = "15/06/2020", "15/06/20", "Monday 15th June 2020"
print(today)
#sys.exit(0)

ddmmyyyy, ddmmyy, full_date = today #each of the three variables have been assigned to that index of the list
print(full_date)
print(ddmmyyyy)