import numpy as np 

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16],
                [17,18,19,20]])

rowwise_sum = np.sum(arr , axis=1)



maxelement_row = np.max(arr , axis=1)

arr[arr < 5] = 0

axis_input = input("Enter the aixs(Press Enter for None): ")

if axis_input == "":
    axis = None
else:
    axis = int(axis_input)

def my_mean(arr , axis=None):


    if axis is None:
        total = np.sum(arr)
        count = arr.size 
        return total/count
    

    total = np.sum(arr , axis=axis)
    count = arr.shape[axis]
    return total / count 
    


print(my_mean(arr , axis))
print(arr)
print(maxelement_row)
print(rowwise_sum)
