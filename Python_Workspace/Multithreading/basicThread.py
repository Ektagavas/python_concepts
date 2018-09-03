# Import threading library
import threading

# Inherit the thread class to create a thread instance
class basicThread(threading.Thread):
    def __init__(self, thname, counter):                # Constructor
        # Create thread instance by calling parent class constructor
        threading.Thread.__init__(self)                 
        self.thname = thname
        self.counter = counter

    # Override the run method
    def run(self):
        while self.counter > 0:
            print('Thread: ', self.thname)
            self.counter -= 1


# Create two new threads with different counters
thread1 = basicThread('thread1', 800000)
thread2 = basicThread('thread2', 500000)

# Schedule the threads
thread1.start()
thread2.start()

# Continue main program execution to check thread behaviour
# for i in range(1,10):
#     print('In main')