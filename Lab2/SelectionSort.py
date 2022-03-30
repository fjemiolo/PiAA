def SelectionSort(A):
    for i in range(len(A)-1):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

from random import randint
A = [randint(1,222) for _ in range (30)]
print(A)
SelectionSort(A)
print(A)