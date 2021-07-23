import threading
import time

my_list = []

def add_to_my_list(start_val, end_val):
    global my_list
    for i in range(start_val, end_val):
        my_list.append(i)
        time.sleep(0.1)

thread1 = threading.Thread(target=add_to_my_list, args=(1, 10))
thread2 = threading.Thread(target=add_to_my_list, args=(10, 20))

threads = [thread1, thread2]
for t in threads:
    t.start()

threads = [thread1, thread2]
for t in threads:
    t.join()

print(my_list)


