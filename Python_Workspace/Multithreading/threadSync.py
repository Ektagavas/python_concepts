# Import threading library
import threading

# Inherit the thread class to create a thread instance
class threadSync(threading.Thread):
    def __init__(self, thname, counter):                # Constructor
        # Create thread instance by calling parent class constructor
        threading.Thread.__init__(self)                 
        self.thname = thname
        self.counter = counter

    # Override the run method
    def run(self):
        # Acquire the lock
        threadLock.acquire()

        # Perform the function
        while self.counter > 0:
            print('Thread: ', self.thname)
            self.counter -= 1
        # Release the lock
        threadLock.release()

# Create new lock
threadLock = threading.Lock()

# Create two new threads with different counters
thread1 = threadSync('thread1', 15)
thread2 = threadSync('thread2', 5)

# Schedule the threads
thread1.start()
thread2.start()

# Wait for the child threads to complete the execution
thread1.join()
thread2.join()

# Continue main program execution to check thread behaviour
for i in range(1,10):
    print('In main')

