import os
import time

def measure_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    return temp.replace("temp=", "")

def main():
    start = time.perf_counter()
    while True:
        print(f'{measure_temp()} after {round(time.perf_counter() - start, 2)} sec')
        time.sleep(1)

if __name__ == '__main__':
    main()
