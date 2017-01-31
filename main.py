import time
from urllib import request
from datetime import datetime
import socket


URL = 'https://google.com'   # out netwrok host
# LOG_INTERVAL = 60            # sec
LOG_INTERVAL = 5             # sec

def main():
    print('Start script at {}'.format(gen_timestamp()))
    print("Status keyword => ['OK', 'NG']")
    while True:
        request_log()
        time.sleep(LOG_INTERVAL)

def request_log():
    hostnames = socket.gethostbyname(socket.gethostname())
    try:
        start = time.time()
        with request.urlopen(URL, timeout=5):
            end = time.time()
            print('{}: OK <{}> {:.3f}ms'.format(gen_timestamp(), hostnames, end - start))
    except:
        print('\033[31m{}: NG <{}>\033[0m'.format(gen_timestamp(), hostnames))


def gen_timestamp():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


if __name__ == '__main__':
    main()
