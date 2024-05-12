import random
import time
c1,c2 = 0,0

def randomized_quicksort(arr):
    global c1

    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        c1 += len(left)+len(right)
        return randomized_quicksort(left) + middle + randomized_quicksort(right)

def quicksort(arr):
    global c2

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1,len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c2 +=1
            else:
                right.append(arr[i])
                c2+=1
        return quicksort(left)+[pivot]+quicksort(right)

arr =[i for i in range(1,111)]
arr1 = arr.copy()
print(f"rand qs   {randomized_quicksort(arr)}\n\n\n comparisions {c1}")
print(f"\n\nnormal qs   {quicksort(arr)}\n\n\n comparisions {c2}")