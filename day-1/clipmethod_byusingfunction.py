import numpy as np

arr = np.arange(15)

max_val = np.max(arr)
min_val = np.min(arr)

#writing a clip method on our own by using basic python functions 
def my_clip(arr , max_val , min_val):
    for n in range(len(arr)):
        if arr[n] < min_val:
            arr[n] = min_val
        elif arr[n] > max_val:
            arr[n] = max_val
    
    return arr

print(my_clip(arr , 11 , 3))

#direct using the clip bulit-in method 
print((arr.clip(3,11)))
