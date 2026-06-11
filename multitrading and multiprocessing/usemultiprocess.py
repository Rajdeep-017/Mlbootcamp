'''
cpu-bound task
 the factorial calculation that we are going to do will we will be doing for larger numbers.

It involves significant computational work.

So with the help of multiprocessing, what we will do is that we will distribute the workload across

multiple CPU cores improving the performance.
'''
import multiprocessing
import math
import sys
import time

#increase the maxi num of digits for integer conversion
sys.set_int_max_str_digits(100000)
#function to compute fact of given num
def compute_fact(num):
    print(f"compute factorial of num")
    res=math.factorial(num)
    print(f"factor {num} : {res}")
    return res
if __name__=="__main__":
    num=[100,32,567,700]
    st=time.time()
    #create the pool of worker processes
    with multiprocessing.Pool() as pool:
        res=pool.map(compute_fact,num)
    end=time.time()
    print(res)
    print(end-st)