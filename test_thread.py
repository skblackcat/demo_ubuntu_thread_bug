#!/usr/bin/python3
import threading
import time
numThread = 1000
def myFunc(number):
	print('Thread-{}'.format(number))
	time.sleep(100)
threadList = [ threading.Thread(target=myFunc,args=(i,)) for i in range( numThread ) ]
for myThread in threadList:
	myThread.start()
print('Sleep..')
time.sleep(100)
