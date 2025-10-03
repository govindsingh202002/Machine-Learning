# import threading
# import time

# def print_num():
#     for i in range(10):
#         print(i)
#         time.sleep(1)
        
# thread=threading.Thread(target=print_num)
# def main():
#    t=time.time()
#    thread.start()
#    thread.join()
#    print(f"completion time is {time.time()-t}seconds")

# if __name__=="__main__":
#     main()



# import multiprocessing
# import time
# def square():
#     for i in range(5):
#         print(f"square {i*i}")
#         time.sleep(1)

# def cube():
#     for i in range(5):
#         print(f"Cube {i*i*i}")
#         time.sleep(1)


# processor1=multiprocessing.Process(target=square)
# processor2=multiprocessing.Process(target=cube)

# def main():
#     t=time.time()
#     processor1.start()
#     processor2.start()
#     processor1.join()
#     print(f"Square completion time {time.time()-t}")
#     processor2.join()
#     print(f"Cube completion time {time.time()-t}")

# if __name__=="__main__":
#     main()


from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def print_num(num):
    print(num)
    time.sleep(1)

numbers=[1,2,3,4,5,6,7,8,9,10]
with ProcessPoolExecutor(max_workers=1) as  executer:
    t= time.time()
    results=executer.map(print_num,numbers)

print(f"time {time.time()-t}")
# for i in results:
#     print(i)