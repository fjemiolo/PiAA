def QuickSort(A, low, high):
    if len(A) == 1:
        return A
    if low < high:
        pi = partition(A, low, high)
        QuickSort(A, low, pi - 1)
        QuickSort(A, pi + 1, high)


def partition(A, low, high):
    i = (low - 1)
    pivot = A[high]

    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1


arr = [13948, 51584, 51258, 17124, 43736, 61659, 47127, 61743, 98326, 33939, 83393, 13269, 48477, 14655, 94493, 45829,
       75496]
QuickSort(arr, 0, len(arr) - 1)

for i in range(len(arr)):
    print(arr[i], end=" ")
