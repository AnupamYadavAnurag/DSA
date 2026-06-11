arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]

<<<<<<< HEAD
print("Sorted array:", arr)
vh
=======
print("Sorted array:")
print(arr)
>>>>>>> 6c934a14923062a35da1a948241af9f98ef99c01
