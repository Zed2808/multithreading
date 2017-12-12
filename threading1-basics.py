import threading
import time
from datetime import datetime

# Define our thread
class MyThread(threading.Thread):

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

        print(f'Exiting {self.name}')

# Initialize two threads
thread1 = MyThread('Thread1')
thread2 = MyThread('Thread2')

# Start both threads
thread1.start()
thread2.start()
