import urllib.request
import time
import threading

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def thread_job(url):
    with lock:
        with urllib.request.urlopen(url) as u:
            return u.read()


lock = threading.Lock()
threads = [threading.Thread(target=thread_job, args=(url, )) for url in urls]

start = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time.time() - start)