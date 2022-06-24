def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


arr = [13948, 51584, 51258, 17124, 43736, 61659, 47127, 61743, 98326, 33939, 83393, 13269, 48477, 14655, 94493, 45829,
       75496]
InsertionSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")

M = "ABCDEFGHQKJSAJKQWHEID"
for i in range(len(M)):
    print(ord(M[i]))
