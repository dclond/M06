"""
David Clond
SDEV 220 M06 Programming Assignment - Concurrency in Python
clond_m06_programming-assignment.py

In your textbook, navigate to the end of Chapters 11 and 16 to the section titled "Things to Do"
Complete the following sections in your Jupyter Notebook:

    13.1
    13.2
    13.3
    15.1

"""

# 13.1 Write the current date as a string to the text file today.txt.
from datetime import date
today = date.today()
today_as_string = today.isoformat()
with open("today.txt", "wt") as output:
    print(today_as_string, file=output)

# 13.2 Read the text file today.txt into the string today_string.
with open("today.txt", "rt") as input:
    today_from_disk = input.read()
print(today_from_disk)

# 13.3 Parse the date from today_string.
from datetime import datetime
formatted_date_template = "%Y-%m-%d\n"
print(datetime.strptime(today_from_disk, formatted_date_template))


# 15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
import multiprocessing

from time import sleep
import random

def dowait(seconds):
    sleep(seconds)
    print("wait time: ", seconds, "the current time is: ", datetime.now())

if __name__ == '__main__':
    for n in range(3):
        seconds = random.random()
        mythread = multiprocessing.Process(target=dowait, args=(seconds,))
        mythread.start()