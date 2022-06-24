def countingSort(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for m in range(0, size):
        count[arr[m]] += 1
    for m in range(1, 10):
        count[m] += count[m - 1]
        m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]


data = [3, 5, 1, 6, 7, 8, 3]
countingSort(data)
print("Sorted Array: ")
print(data)
