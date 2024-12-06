x = [1,2,3,4,5]
y = []
z = []

y.append(x.pop())
y.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.sort()

print("x = ",x)
print("y = ",y)
print("z = ",z)
print()

arr1 = [1, 2,21,33,45,65,12]
print("INSERTION SORT ALGORITHM")
print("Arr1 values before Insertion Sort: ")
print(arr1)
for i in range(1, len(arr1)):
    key = arr1[i]
    j = i - 1
    while j >= 0 and key > arr1[j]:
        arr1[j+1] = arr1[j]
        j-=1
    arr1[j+1] = key

print("Arr1 values after Insertion Sort: ")
print(arr1)
print()
print()


arr2 = [1, 2,21,33,45,65,12]
print("SELECTION SORT ALGORITHM")
print("Arr2 values before Selection Sort")
print(arr2)
for i in range(len(arr2)):
    min_idx = i
    for j in range(i + 1, len(arr2)):
        if arr2[j] < arr2[min_idx]:
            min_idx = j
    arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
print("All arrays values after Selection Sort: ")
print(arr2)
print()