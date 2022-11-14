import multiprocessing


def worker():
    LIST.append('item')


LIST = [] # процелл создает копию, поэтому в этот диск ничего не записывается


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker)
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)