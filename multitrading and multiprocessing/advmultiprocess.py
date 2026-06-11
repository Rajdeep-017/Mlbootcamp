from concurrent.futures import ProcessPoolExecutor
import time

def sq_num(num):
    time.sleep(1)
    return f"num : {num*num}"

num=[1,2,3,4,5]
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor: #multiple threads =3
        results=executor.map(sq_num,num)

    for res in results:
        print(res)
