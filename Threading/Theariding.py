import threading
import time

def clock(interval):
    while True:
        print('Поток {} времени {} Время не остановить'.format(threading.get_ident(), time.ctime()))
        time.sleep(interval)

if __name__ == '__main__':
    t1 = threading.Thread(target=clock, args=(5,))
    t2 = threading.Thread(target=clock, args=(2,))
    t1.start()
    t2.start()