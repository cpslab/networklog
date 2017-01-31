import time
from urllib import request
from datetime import datetime
import traceback

# out netwrok host
URL = 'https://google.com'

# sec
LOG_INTERVAL = 60

def main():
    while True:
        request_log()
        time.sleep(LOG_INTERVAL)

def request_log():
    try:
        with request.urlopen(URL):
            print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            print()
    except:
        traceback.print_exc()
        exit()

if __name__ == '__main__':
    main()
