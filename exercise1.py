from multiprocessing import Process
import os
num = os.path.getsize("2020-07-10.jpeg")

def top_photo():
    with open("2020-07-10.jpeg","rb") as f:
        with open("top.jpeg","wb") as b:
            n = num//2
            while n > 1024:
                b.write(f.read(1024))
                n-=1024
            else:
                b.write(f.read(n))
def bit_photo():
    with open("2020-07-10.jpeg","rb") as f:
        with open("bit.jpeg","wb") as b:
            f.seek(num//2)
            while True:
                date = f.read(1024)
                if not date:
                    break
                b.write(date)
p = Process(target=top_photo)
p.start()
bit_photo()
p.join()

