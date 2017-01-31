import time
from urllib import request
from datetime import datetime
import socket

# out netwrok host
URL = 'https://google.com'

# sec
LOG_INTERVAL = 60


def main():
    print('Start script at {}'.format(gen_timestamp()))
    print("Status keyword => ['OK', 'NG']")
    while True:
        request_log()
        time.sleep(LOG_INTERVAL)

def request_log():
    hostnames = socket.gethostbyname(socket.gethostname())
    try:
        with request.urlopen(URL):
            print('{}: OK <{}>'.format(gen_timestamp(), hostnames))
    except:
        print('\033[31m{}: NG <{}>\033[0m'.format(gen_timestamp(), hostnames))

def gen_timestamp():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


if __name__ == '__main__':
    main()
