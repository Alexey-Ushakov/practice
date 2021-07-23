import time
from threading import Thread, Semaphore, get_ident

s = Semaphore(5)
# Если не передавать в Semaphore параметр,
# семафор будет инициализирован 1
# (и таким образом станет обычной блокировкой)
current_readers = []


def subscribe(interval):
    global current_readers
    while True:
        s.acquire()
        current_readers.append(get_ident())
        time.sleep(interval)
        current_readers.remove(get_ident())
        s.release()


def check(interval):
    global current_readers
    while True:
        print(current_readers)
        time.sleep(interval)


if __name__ == '__main__':
    threads = (Thread(target=subscribe, args=(1,))
               for _ in range(10))
    check_thread = Thread(target=check, args=(3,))
    for t in threads:
        t.start()
    check_thread.start()
