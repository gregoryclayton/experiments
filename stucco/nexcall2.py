
import time


infiniteloop = True

while infiniteloop:

    with open('C:/Users/grego/Desktop/pros2/stucco/log3.txt','r') as f:
        for line in f:
            print(line.strip())
            time.sleep(.5)
