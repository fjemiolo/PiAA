def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 10:
        countingSort(arr, exp)
        exp *= 10


arr = [13948, 51584, 51258, 17124, 43736, 61659, 47127, 61743, 98326, 33939, 83393, 13269, 48477, 14655, 94493, 45829,
       75496]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
