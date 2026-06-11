from concurrent.futures import ThreadPoolExecutor
import time

def print_num(num):
    time.sleep(1)
    return f"num : {num}"

num=[1,2,3,4,5,6,5,6,7,8,9,0]
with ThreadPoolExecutor(max_workers=3) as executor: #multiple threads =3
    results=executor.map(print_num,num)

for res in results:
        print(res)
