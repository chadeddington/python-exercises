from datetime import datetime

def main():
	now = datetime.now()
	# datetime control string
	print now.strftime("%x")

if __name__ == "__main__":
  main();
