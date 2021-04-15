import threading
import time


def do(event):
    print('start')
    event.wait()
    print('end')


if __name__ == "__main__":
    event_obj = threading.Event()  # 创建一个事件
    event_obj.clear()

    t1 = threading.Thread(target=do, args=(event_obj,))
    t1.start()

    data = input('请输入要：')
    if data == 'True':
        event_obj.set()  # 变绿灯

    time.sleep(5)
