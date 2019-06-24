import threading, time, random


my_mutex = threading.Lock()
class Thread_One(threading.Thread):

    def run(self):
        global my_mutex
        print('The first thread is now sleeping.')
        time.sleep(random.randint(1, 5))
        print('The first thread is now finished.')
        my_mutex.release()


class Thread_Two(threading.Thread):

    def run(self):
        global my_mutex
        print('The second thread is now sleeping.')
        time.sleep(random.randint(1, 5))
        my_mutex.acquire()
        print('The second thread is now finished.')

my_mutex.acquire()
t1 = Thread_One()
t2 = Thread_Two()

t1.start()
t2.start()
