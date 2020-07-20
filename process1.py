from multiprocessing import Process
from time import sleep

def func(name,score):
    for i in range(2):
        sleep(1)
        print(name*i)
        sleep(1)
        score += 1
        print(score)

p = Process(target = func,args=("wang",99))

p.start()
p.join()