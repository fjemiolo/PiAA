def BubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


arr = [13948, 51584, 51258, 17124, 43736, 61659, 47127, 61743, 98326, 33939, 83393, 13269, 48477, 14655, 94493, 45829,
       75496]
BubbleSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
