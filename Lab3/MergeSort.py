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

