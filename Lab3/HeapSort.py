def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


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
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapify(A, 0, i - 1)


A = [1, 3, 1, 2, 7, 9, 1, 6, 1, 0, 4, 2]
print(f"A: {A}")
HeapSort(A, len(A))
print(f"Sorted A: {A}")
B = [15, 3, 99, 1, 25, 7, 9, 9, 1, 100, 6, 1, 0, 12, 4, 2, 9, 0, 87, 122, 54]
print(f"B: {B}")
HeapSort(B, len(B))
print(f"Sorted B: {B}")
C = [0, 12, 4, 2, 9, 0, 87, 122, 54, 1, 2, 11, 55, 99]
print(f"C: {C}")
HeapSort(C, len(C))
print(f"Sorted C: {C}")



# incorrect build heap
"""
def heapify(arr, n, i):
 
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l
 
    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r
 
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
 
# Function to build a Max-Heap from the given array
 
 
def buildHeap(arr, n):
 
    # Index of last non-leaf node
    startIdx = n // 2 - 1
 
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -2):
        heapify(arr, n, i)
        
        
A = [56, 24, 76, 179, 1, 164, 138, 154, 57, 108, 26, 197, 142, 11, 90, 20, 91, 60, 129, 59]
print(A)
buildHeap(A, len(A))
print(A)
for i in range (20):
    print(f'A[{i+1}] = {A[i]}')
    """