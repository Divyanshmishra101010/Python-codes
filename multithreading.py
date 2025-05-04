import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def func(seconds):
    time.sleep(seconds)
    return seconds


# Method 1

# start = datetime.now()

# t1 = threading.Thread(target=func, args=[3])
# t2 = threading.Thread(target=func, args=[3])
# t3 = threading.Thread(target=func, args=[3])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# end = datetime.now()
# print(end-start)


# Method 2

ans = []
seconds = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        task = [executor.submit(func, second) for second in seconds]

        for future in task:
            res = future.result()
            ans.append(res)
    
    print(ans)

start = datetime.now()
poolingDemo()
end = datetime.now()
print(end-start)