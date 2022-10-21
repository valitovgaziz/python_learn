import sys
import time

f = None
try:
	f = open("poem.txt")
	# Our ussual file_reading idiom
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end='')
		sys.stdout.flush()
		print("Press ctrl_c now")
		# Tomake sure it runs for a while
		time.sleep(2)
except IOError:
	print("Could not find file poem.txt")
except KeyboardInterrupt:
	print("!! You cnacelled the reading from the file.")
finally:
	if f:
		f.close()
	print("(Cleaning up: Close the file)")
