import time
from random import randint
import threading


def runtime(function):

    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        print(time.time() - start)

    return wrapper


@runtime
def summation(arr):
    summ = 0
    for num in arr:
        summ += num
    print(summ)


@runtime
def multithreading_summation(arr):
    def thread_job(index, count):
        with lock:
            global summ
            for i in range(index, index + count):
                summ += arr[i]

    threads = [threading.Thread(target=thread_job, args=(i * 10 ** 5, 10 ** 5)) for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(summ)


arr = [randint(0, 10 ** 8) for i in range(10 ** 6)]
print(summation(arr))

lock = threading.Lock()
summ = 0
print(multithreading_summation(arr))