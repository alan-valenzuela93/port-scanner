import socket


def banner_grabbing(addr, port):
    print("Getting service information for open TCP/IP port: ", port + "...")
    socket.setdefaulttimeout(10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((addr, port))
    data = ''
    headers = \
        "GET / HTTP/1.1\r\n" \
        f"Host: {addr}\r\n" \
        "User-Agent: python-custom-script/2.22.0\r\n" \
        "Accept-Encoding: gzip, deflate\r\nAccept: */*\r\n" \
        "Connection: keep-alive\r\n\r\n"
    print("\n\n" + headers)
    cycle = True

    try:  # If banner can't be reach, print a message
        while cycle:  # Keep looping until the banner is found
            data = str(s.recv(4096))
            if data != '':
                s.send(headers.encode())  # Send request
                cycle = False
            s.close()
    except:
        print("Connection refused... banner unreachable")

    return data + '\n'
