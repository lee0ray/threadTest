import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.balance = balance


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    if account.balance >= draw_amount:
        # 吐出钞票
        print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
        # time.sleep(0.001)
        # 修改余额
        account.balance -= draw_amount
        print("\t余额为: " + str(account.balance))
    else:
        print(threading.current_thread().name + "取钱失败！余额不足！")


if __name__ == '__main__':
    # 创建一个账户
    acct = Account("1234567", 1000)
    # 模拟两个线程对同一个账户取钱
    threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
    threading.Thread(name='乙', target=draw, args=(acct, 800)).start()

# class X:
#     #定义需要保证线程安全的方法
#     def m () :
#         #加锁
#         self.lock.acquire()
#         try :
#             #需要保证线程安全的代码
#             ＃...方法体
#         #使用finally 块来保证释放锁
#         finally :
#             #修改完成，释放锁
#             self.lock.release()