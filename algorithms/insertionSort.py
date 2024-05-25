# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
from colors import *


def insertion_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(1,size):
        key = data[i]
        j = i - 1

        while(j >=0 and data[j] > key):
            data[j + 1] = data[j]
            j = j - 1
            drawData(data, [PURPLE if x == j + 1 else YELLOW  if x == i else BLUE for x in range(len(data))])
            time.sleep(timeTick)
        data[j + 1] = key
          

    drawData(data, [BLUE for x in range(len(data))])