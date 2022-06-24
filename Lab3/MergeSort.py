'''
def MergeSort(A, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    MergeSort(A, left, mid)
    MergeSort(A, mid + 1, right)
    merge(A, left, mid, right)


def merge(A, left, mid, right):
    L = A[left:mid + 1]
    R = A[mid + 1:right + 1]
    main_cnt = left
    cnt_l = cnt_r = 0
    while cnt_l < len(L) and cnt_r < len(R):
        if cnt_l > cnt_r:
            A[main_cnt] = R[cnt_r]
            cnt_r += 1
        else:
            A[main_cnt] = L[cnt_l]
            cnt_l += 1
        main_cnt += 1
    while cnt_l < len(L):
        A[main_cnt] = L[cnt_l]
        main_cnt += 1
        cnt_l += 1
    while cnt_r < len(R):
        A[main_cnt] = R[cnt_r]
        main_cnt += 1
        cnt_r += 1
'''


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [13948, 51584, 51258, 17124, 43736, 61659, 47127, 61743, 98326, 33939, 83393, 13269, 48477, 14655, 94493, 45829,
       75496]
mergeSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
