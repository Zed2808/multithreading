import threading
import time
from datetime import datetime

# Define our thread
class TriggerThread(threading.Thread):

    # Initialize the thread with a name
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    # Define what our thread should do
    def run(self):
        print(f'Starting {self.name}')

        # Print time 3 times
        for i in range(3):
            print(f'{self.name}: {datetime.now()}')
            time.sleep(1)

        # Trigger even once task is completed
        print('Triggering event')
        event.set()

        print(f'Exiting {self.name}')

class WaitingThread(threading.Thread):

    # Initialize the thread with a name
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    # Define what our thread should do
    def run(self):
        print(f'Starting {self.name}')

        # Wait for event to be triggered before starting task
        print('Waiting for event')
        event.wait()
        print('Event detected')

        # Print time 3 times
        for i in range(3):
            print(f'{self.name}: {datetime.now()}')
            time.sleep(1)

        print(f'Exiting {self.name}')

# Create event object
event = threading.Event()

# Initialize two threads
thread1 = TriggerThread('Thread1')
thread2 = WaitingThread('Thread2')

# Start both threads
thread1.start()
thread2.start()
