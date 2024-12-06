x=[1, 2, 3, 4, 5]
y=[]
z=[]

y.append(x.pop())
y.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.sort()

print(x, y, z)

def insertion_sort(X):
    for i in range(1, len(X)):
        key = X[i]
        j = i - 1
        while j >= 0 and X[j] < key:
            X[j + 1] = X[j]
            j -= 1
        X[j + 1] = key

def selection_sort(X):
    for i in range(len(X)):
        min_idx = i
        for j in range(i+1, len(X)):
            if X[j] < X[min_idx]:
                min_idx = j
        X[i], X[min_idx] = X[min_idx], X[i]


X = [1, 2, 21, 33, 45, 65, 12]
insertion_sort(X)
print(X)
selection_sort(X)
print(X)