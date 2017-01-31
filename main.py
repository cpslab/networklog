import time
from urllib import request
from datetime import datetime
import socket


URL = 'https://google.com'   # out netwrok host
LOG_INTERVAL = 60            # sec
# LOG_INTERVAL = 1             # sec

def main():
    message = "Start script at {}\nStatus keyword => ['OK', 'NG']\n".format(gen_timestamp())
    with open(get_filename(), 'a') as f:
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
        message = '{}: NG <{}>'.format(gen_timestamp(), hostnames)
        # message = '\033[31m{}: NG <{}>\033[0m'.format(gen_timestamp(), hostnames)
    with open(get_filename(), 'a') as f:
        f.write(message + "\n")

def get_filename():
    return datetime.now().strftime("/home/pi/logs/%Y%m%d.log")

def gen_timestamp():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

if __name__ == '__main__':
    main()
