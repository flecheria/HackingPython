import os
from xml.sax.saxutils import prepare_input_source

def child_process():
    print("i-m the child process and my PID is %d" % os.getpid())
    print("esc from child process")

def parent_process():
    print("i-m the parent process, make the fork")
    # this replicate the current process, is exaclty the same process
    child_pid = os.fork()

    if child_pid == 0:
        print("we are inside the child")
        child_process()
    else:
        print("we are inside the parent process")
        print("i-m the parent process and my PID is %d" % os.getpid())

    while True:
        pass

if __name__ == "__main__":
    parent_process()