import time
from urllib import request
from datetime import datetime
import socket


URL = 'https://google.com'   # out netwrok host
LOG_INTERVAL = 60            # sec
# LOG_INTERVAL = 1             # sec

def main():
    message = 'Start script at {}'.format(gen_timestamp()) + "\nStatus keyword => ['OK', 'NG']"
    with open(get_filename(), 'w') as f:
        f.write(message)

    while True:
        request_log()
        time.sleep(LOG_INTERVAL)

def request_log():
    hostnames = socket.gethostbyname(socket.gethostname())
    try:
        start = time.time()
        with request.urlopen(URL, timeout=5):
            end = time.time()
            message = '{}: OK <{}> {:.3f}ms'.format(gen_timestamp(), hostnames, end - start)
    except:
        message = '\033[31m{}: NG <{}>\033[0m'.format(gen_timestamp(), hostnames)
    with open(get_filename(), 'w') as f:
        f.write(message)

def get_filename():
    return datetime.now().strftime("logs/%Y%m%d.log")

def gen_timestamp():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

if __name__ == '__main__':
    main()
