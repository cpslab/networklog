import time
from urllib import request
from datetime import datetime

# out netwrok host
URL = 'https://google.com'

# sec
LOG_INTERVAL = 60

def main():
    while True:
        request_log()
        time.sleep(LOG_INTERVAL)

def request_log():
    timestamp_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    try:
        with request.urlopen(URL):
            print(timestamp_str + ':OK')
    except:
        print('\033[31m{}:Error\033[0m'.format(timestamp_str))

if __name__ == '__main__':
    main()
