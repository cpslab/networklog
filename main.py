import time
from urllib import request
from datetime import datetime
import socket

# out netwrok host
URL = 'https://google.com'

# sec
LOG_INTERVAL = 60


def main():
    while True:
        request_log()
        time.sleep(LOG_INTERVAL)

def request_log():
    hostnames = socket.gethostbyname(socket.gethostname())
    timestamp_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    try:
        with request.urlopen(URL):
            print('{}: OK <{}>'.format(timestamp_str, hostnames))
    except:
        print('\033[31m{}: NG <{}>\033[0m'.format(timestamp_str, hostnames))

if __name__ == '__main__':
    main()
