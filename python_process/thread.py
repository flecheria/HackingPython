#!/usr/bin/env python

# import thread
import threading
import time

def worker_thread(id):
    count = 1
    while True:
        print("thread with ID {0} has counter value {1}".format(id, count))
        time.sleep(1)
        count += 1

if __name__ == "__main__":
    for i in range(5):
        # python 2 implementation
        # thread.start_new_thread(worker_thread, (i, ))

        # python 3 implementation
        threading.Thread(target=worker_thread, 
            args=(1, )
        ).start()

    print("Main thread going to infinite loop")
    while True:
        pass