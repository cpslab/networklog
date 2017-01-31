import time
from datetime import datetime
import socket
import os


HOST = 'google.com'   # out netwrok host
LOG_INTERVAL = 60            # sec
# LOG_INTERVAL = 1             # sec

def main():
    message = "Start script at {}\nStatus keyword => ['OK', 'NG']\n".format(gen_timestamp())
    with open(get_filename(), 'a') as f:
        f.write(message)

    while True:
        request_log()
        time.sleep(LOG_INTERVAL)

def is_live():
    response = os.system("ping -c 1 " + HOST + " }&/dev/null")
    return response == 0

def request_log():
    hostnames = socket.gethostbyname(socket.gethostname())
    if is_live():
        message = '{}: OK <{}>'.format(gen_timestamp(), hostnames)
    else:
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
