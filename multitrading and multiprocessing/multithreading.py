#multithreading
#when to use
#reasons -I/O bound tasks:  Task that spends more time waiting for I o operation file operation or network request.
#concurrent exceution:concurrent execution, when you want to improve the throughput of your application by performing multiple operation concurrently.
import threading
import time
def print_num():
    for i in range(5):
        time.sleep(2)
        print(i)
def print_let():
    for l in "abcde":
        time.sleep(2)
        print(l)
#creat 2 thread
t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_let)
t=time.time()
#start thred
t1.start()
t2.start()
#wait for thread to complete
t1.join()
t2.join()
finish=time.time()-t
print(finish)
