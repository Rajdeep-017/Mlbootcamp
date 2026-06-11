#It allows you to create processes that runs in parallel.
#when to use cpu-bound task: mathe task
#parallel exceution:multiple cores in CPU
import multiprocessing
import time
def sqnum():
    for i in range(5):
        time.sleep(1)
        print("squ", i**2)

def cubenum():
    for i in range(5):
        time.sleep(1)
        print(i**3)
if __name__ == "__main__":
    #create 2 processes
    p1=multiprocessing.Process(target=sqnum)
    p2=multiprocessing.Process(target=cubenum)
    t=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish=time.time()-t
    print(finish)

    



