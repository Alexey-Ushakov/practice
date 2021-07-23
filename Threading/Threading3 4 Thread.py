import threading
import time

def process():
    time.sleep(2)


start = time.time()
threads = [threading.Thread(target =process) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print('for runs took {}'.format(time.time() - start))