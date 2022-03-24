def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def BuildMaxHeap(A, n):
    for i in range(n, -1, -1):
        MaxHeapify(A, i, n)


def MaxHeapify(A, i, n):
    if left(i) < n and A[left(i)] > A[i]:
        largest = left(i)
    else:
        largest = i
    if right(i) < n and A[right(i)] > A[largest]:
        largest = right(i)
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest, n)


def HeapSort(A, n):
    BuildMaxHeap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapify(A, 0, i-1)


A = [1,3,1,2,7,9,1,6,1,0,4,2]
print(f"A: {A}")
HeapSort(A, len(A))
print(f"Sorted A: {A}")
B = [15,3,99,1,25,7,9,9,1,100,6,1,0,12,4,2,9,0,87,122,54]
print(f"B: {B}")
HeapSort(B, len(B))
print(f"Sorted B: {B}")
C = [0,12,4,2,9,0,87,122,54,1,2,11,55,99]
print(f"C: {C}")
HeapSort(C, len(C))
print(f"Sorted C: {C}")