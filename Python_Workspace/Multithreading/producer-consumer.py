import threading

itemCount = 0
BUFFER_SIZE = 10

# Producer class
class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    # Method to produce an item
    def produce(self):
        global itemCount
        global BUFFER_SIZE
        print('Producing...')
        self.add_item()                                     # Produce an item
    
    # Add an item
    def add_item(self):
        global itemCount
        threadLock.acquire()                                # Acquire lock
        if itemCount < BUFFER_SIZE:
            itemCount += 1
            print('Added an item ===> ', itemCount)
        threadLock.release()                                # Release lock

    def run(self):
        while True:
            self.produce()
    

# Consumer class
class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    # Consume an item
    def consume(self):
        global itemCount
        print('Consuming....')
        self.remove_item()                                  # Consume a item
    
    # Remove an item
    def remove_item(self):
        global itemCount
        threadLock.acquire()                                # Acquire lock
        if itemCount > 0:
            itemCount -= 1
            print('Removed an item ===> ', itemCount)
        threadLock.release()                                # Release lock

    def run(self):
        while True:
            self.consume()


# Create new lock
threadLock = threading.Lock()

# Create producer consumer instances
producer = Producer()
consumer = Consumer()

# Start the thread
producer.start()
consumer.start()