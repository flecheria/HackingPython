#!/usr/bin/env python

import threading
import time
from queue import Queue;

class WorkerThread(threading.Thread):

    def __init__(self, queue) -> None:
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print("I-m worker thread")
        while True:
            counter = self.queue.get()
            print("ordered to sleep for {} seconds".format(counter))
            time.sleep(counter)
            print("finish to sleep for {} seconds".format(counter))
            self.queue.task_done()

if __name__ == "__main__":
    queue = Queue()

    for i in range(10):
        print("creating worker thread {}".format(i))
        wt = WorkerThread(queue)
        wt.setDaemon(True)
        wt.start()
        print("orker thread {} created".format(i))

    for j in range(10):
        queue.put(j)

    queue.join()
    print("all task over")