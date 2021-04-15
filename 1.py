import threading
import gc
import time

print(gc.isenabled())
print(threading.active_count())
print(threading.current_thread())
print(threading.get_ident())

mydata = threading.local()
mydata.x = 1


def fn1(a):

    print(a)


def song(a, b, c):
    print(a, b, c)
    for i in range(5):
        print("song")
        time.sleep(1)


if __name__ == '__main__':
    t = threading.Thread(target=fn1, args=(1,))
    t.start()
    t.s
    print(mydata)
    # fn1(1)
    # threading.Thread(target=song, args=(1, 2, 3)).start()
