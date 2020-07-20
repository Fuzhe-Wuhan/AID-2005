import multiprocessing
from time import sleep


# 进程执行函数
def func():
    print("num2 start")
    sleep(2)
    print("over")
# 创建进程对象
p = multiprocessing.Process(target=func)
# 启动进程 执行函数
p.start()
# 等待完成后回收
p.join()
