arr = [3,4,7,8,2,1]
n = len(arr)
# print(n)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


# Insertion Sort

arr = [3,4,7,8,2,1]
n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print(arr) 