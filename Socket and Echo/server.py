import socket
import time
import json


host = '0.0.0.0'
port = 35200
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
quit = False
print('[Server Started]')

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        itsattime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())
        addr = {'ipaddres' : [addr[0], addr[1]],
                'time': itsattime
        }
        data = {

        }
        print(json.dumps(addr), end="")
        print(data.decode('utf-8'))
        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except Exception as ex:
        print(ex)
        print('\n[ Server Stopped ]')
        quit = True

s.close()
