arr1 = [23,89, 7, 56, 44]
print("Arr1 values before Bubble Sort: ")
print(arr1)
for i in range(len(arr1)):
    for j in range(0, len(arr1) - i - 1):
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
print("Arr1 values after Bubble Sort: ")
print(arr1)
print()


arr2 = [12, 78, 91, 34, 62]
print("Arr2 values before Insertion Sort: ")
print(arr2)
for i in range(1, len(arr2)):
    key = arr2[i]
    j = i - 1
    while j >= 0 and key < arr2[j]:
        arr2[j+1] = arr2[j]
        j-=1
    arr2[j+1] = key
print("Arr2 values after Insertion Sort: ")
print(arr2)
print()

arr3 = [5, 99, 48, 15, 67]
print("Arr3 values before Insertion Sort: ")
print(arr3)
for i in range(1, len(arr3)):
    min_idx = i
    for j in range(i - 1, len(arr3)):
        if arr3[min_idx] > arr3[j]:
            min_idx = j
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]
print("Arr3 values after Insertion Sort: ")
print(arr3)
print()

arr4 = [38, 82, 25, 74, 13]
print("Arr4 values before Insertion Sort: ")
print(arr4)
for i in range(1, len(arr4)):
    key = arr4[i]
    j = i - 1
    while j >= 0 and key > arr4[j]:
        arr4[j+1] = arr4[j]
        j-=1
    arr4[j+1] = key
print("Arr4 values after Insertion Sort: ")
print(arr4)
print()


Arr5 = [arr1[2], arr1[3], arr2[2], arr2[3], arr3[2], arr3[3],arr4[2], arr4[3]]
newArr5 = Arr5
for i in range(1, len(newArr5)):
    key = newArr5[i]
    j = i - 1
    while j >= 0 and key < newArr5[j]:
        newArr5[j+1] = newArr5[j]
        j-=1
    newArr5[j+1] = key
print("Ascending order of Arr5: ")
print(newArr5)
for i in range(1, len(newArr5)):
    key = newArr5[i]
    j = i - 1
    while j >= 0 and key > newArr5[j]:
        newArr5[j+1] = newArr5[j]
        j-=1
    newArr5[j+1] = key
print("Descending order of Arr5: ")
print(newArr5)
print()


allArrays = arr1 + arr2 + arr3 + arr4
print("All arrays from numbers 1 - 4: ")
print(allArrays)
for i in range(len(allArrays)):
    min_idx = i
    for j in range(i + 1, len(allArrays)):
        if allArrays[j] < allArrays[min_idx]:
            min_idx = j
    if min_idx != i:
        temp = allArrays[i]
        allArrays[i] = allArrays[min_idx]
        allArrays[min_idx] = temp
print("All arrays values after Selection Sort: ")
print(allArrays)
print()

arr7 = allArrays
print("Array lists form 1 - 4: ")
print(arr7)
print("Even Values: ")
for num in arr7:
    if num % 2 == 0:
        print(num, end =" ")
print()
print("Odd Values: ")
for num in arr7:
    if num % 2 != 0:
        print(num, end =" ")





"""#Insertion Sort
arr1 = [10, 2, 3, 1, 1, 4, 89, 21]
#printing the values arr1
print("Arr1 values before Insertion Sort: ")
print(arr1)
def InsertionSort(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        # Move elements of array [0...i-1]
        # that are grater than the key
        # to one position ahead of
        # their current position
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key
        
print("Arr1 values after Insertion Sort: ")
print(arr1)
print("\n")

#Selection Sort
arr2 = [10, 2,3, 1, 1, 4, 89, 21]
print("Arr2 before Selection Sort: ")
print(arr2)
def SelectionSort(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
            # swapping the values from our array
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
    print("Arr2 values after Selection Sort: ")
    print(arr2)

print("\n")
#Bubble Sort
arr3 = [10, 2,3, 1, 1, 4, 89, 21]
print("Arr3 values before Bubble Sort: ")
print(arr3)
def BubbleSort(arr3):
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
print("Arr3 values after Bubble Sort: ")
print(arr3)"""