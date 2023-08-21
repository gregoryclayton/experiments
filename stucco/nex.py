
import subprocess
import os
import time

def spinning_cursor(step):
    for d in range(step):    
        for cursor in '\\|/-':
            time.sleep(0.1)
            print(f"\r{cursor}", end="", flush=True)

def progress_bar():
  for i in range(101):
    time.sleep(0.1)
    print(f"\r{i:02d}: {'#'*(i//2)}", end="", flush=True)
    # print(f"\r{i:02d}: [{'#'*(i//2)}{'='*(50-(i//2))}>]", end="", flush=True) #fancier pbar

infiniteloop = True

print("***************************************************")
print("***************************************************")
print("************NETWORK GOD MONTORING TOOLS************")
print("***************************************************")
print("***************************************************")
time.sleep(1)
print("initializing...")
time.sleep(1)
print("initializing...")
time.sleep(1)
print("initializing...")
time.sleep(1)
spinning_cursor(2)
print("connected")
time.sleep(0.75)



(input("username:"))
(input("password:"))
spinning_cursor(6)


print("/")
print("*************************")
print("***WELCOME BACK STUCCO***")
print("*************************")

time.sleep(2)


os.startfile("C:/Users/grego/Desktop/pros2/stucco/nexcall2.py")
time.sleep(0.3)
os.startfile("C:/Users/grego/Desktop/pros2/stucco/nexcall.py")
#subprocess.run(["python", "C:/Users/grego/Desktop/pros2/stucco/nexcall.py"])



with open('C:/Users/grego/Desktop/pros2/stucco/log2.txt','r') as f:
    for line in f:
        print(line.strip())
        time.sleep(2)

os.startfile("C:/Users/grego/Desktop/pros2/stucco/nex2.py")

