#
# Example file for working with timedelta objects
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

ayear = timedelta(days=365)
now = datetime.now()

# Todays date a year from now
# print "One year from now it will be " + str(now + ayear);

# One week ago
t = now - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
# print "A week from now it was " + s

# Days until Christmas
today = date.today()
christmas = date(today.year, 12, 25)

# String arguments for injecting a variable
print "Christmas is %s days away" % (christmas - today).days 