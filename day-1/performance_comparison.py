import time
import numpy as np

arr = np.random.rand(1000000)

total = 0
start = time.time()
for a in arr:
    total += a

mean_loop = total / len(arr)

end = time.time()

start_vector = time.time()

mean = np.sum(arr) / arr.size

end_vector = time.time()

print("Time taken by loop : " , end - start)
print("Time takesn by numpy: " , end_vector - start_vector)
