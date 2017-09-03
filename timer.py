#Dependencies
import sys
import string
import time
from time import sleep

'''
If you would like to use this program the easiest way to do so is to download this onto your computer and run it from your terminal.
If you would like to use the timer without setting a beep at a certain interval, then type in "python timer.py TIMER_DURATION".
If you would like to use the timer with an interval, then type in "python timer.py TIMER_DURATION INTERVAL_TIME.
Note: TIMER_DURATION refers to how long you want the entire timer to last for. INTERVAL_TIME refers to how much time do you want to
pass in between the beeps. For example, if you want there to be a beep every minute for 30 minutes type in: "python timer.py 30 1".
'''

#Set variables
arg = sys.argv
larg = len(sys.argv)

#Make sure there are only two or three arguments
if  larg != 2 and larg != 3:
    print("There is an invalid number of arguments. Use either two or three arguments.")
    sys.exit(1)

#Setting minutes
minutes = arg[1]

#Making sure the minutes is an integer
try:
    minutes = int(minutes)
except ValueError:
    print("Please enter integer values")
    sys.exit(1)

#See if there is a third argument for interval time
try:
    #Setting interval time
    interval_time = arg[2]
    print(interval_time)
    x = 5
    if interval_time == 0: #Ignoring the value if it is zero
        x = 4
except Exception as e:
    x = 4
    print("no interval")
    pass

#Making sure interval_time is an integer
if x == 5:
    try:
        interval_time = int(interval_time)
    except ValueError:
        print("Please enter integer values")
        sys.exit(1)

#Setting seconds
seconds = minutes * 60

#Execution of timer without an interval
if x == 4:
    print("no interval")
    try:
        if minutes > 0:
            print "Sleeping for " + str(minutes)
            n_seconds = float(seconds)
            sleep(n_seconds)
        print "Wake up"
        for i in range(6):
            print chr(7),
            sleep(1)
        else:
            print("DONE")
            sys.exit(1)
    except KeyboardInterrupt:
        print ("Interrupted by user")
        sys.exit(1)

#Execution of timer with interval
if x == 5:
    print("interval")
    try:
        if minutes > 0:
            t_end = time.time() + seconds
            print "Sleeping for " + str(minutes)
            print "Beep every" + str(interval_time)
            while time.time() < t_end:
                n_seconds = float(interval_time*60)
                sleep(n_seconds)
                print chr(7)
        print "Wake up"
        for i in range(6):
            print chr(7),
            sleep(1)
        else:
            print("DONE")
            sys.exit(1)
    except KeyboardInterrupt:
        print ("Interrupted by user")
        sys.exit(1)
