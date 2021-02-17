import socket
import argparse
from grabber import banner_grabbing

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Enter your target address', required=True)
parser = parser.parse_args()
ports = [21, 22, 25, 53, 66, 80, 88, 110, 139, 443, 445, 8080, 9050]  # These are some of the most interesting ports to scan


def get_ip(target):
    return str(socket.gethostbyname(target))


def scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.settimeout(0.2)  # Increase scanning speed
    except:
        return False
    else:
        return True


def main():
    for p in ports:
        if scan(parser.target, p):
            print(banner_grabbing(parser.target, p))


if __name__ == '__main__':
    print('TCP/IP scan started at IP ' + get_ip(parser.target))
    main()
