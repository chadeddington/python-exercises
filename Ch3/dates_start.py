# From the datetime MODULE import the date, time, and datetime CLASSES
from datetime import date
from datetime import datetime

def getDay(i):
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	return days[i]

def main():
	# today = date.today()
	today = datetime.now()
	#currentTime = datetime.time(datetime.now())
	# print "The current time is ", currentTime
	print "Today is" ,getDay(date.weekday(today))

# When running file from the commandline
if __name__ == "__main__":
  main();
  