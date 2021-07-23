import socket
import threading
import time
import json

shutdown = False
join = False

def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode('utf-8'))
                time.sleep(0.2)
        except:
            pass

server = ('localhost', 35200)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 0))

name = input('Name: ')

rT = threading.Thread(target=receving, args=('RecvThread', s))
rT.start()
itsattime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())
while not shutdown:
    if not join:
        data = {"time": itsattime,
                'name': name,
                "join": "join the chat"
                }
        s.sendto(json.dumps(data).encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()
            if message != "":
                data = {"time": itsattime,
                        'name': name,
                        'message': message
                        }
                s.sendto(json.dumps(data).encode("utf-8"), server)
            time.sleep(0.2)
        except:
            s.sendto(('[' + name + '] :: ' + message).encode('utf-8'), server)
            shutdown = True

rT.join()
s.close()