import os

if __name__ == "__main__":
    # this interrupt the parent process
    # the original process is overlay
    os.execvp("ping", ["ping", "127.0.0.1"])