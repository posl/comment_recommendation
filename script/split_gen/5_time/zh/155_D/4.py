def get_sort_list(N, K, A):
    sort_list = []
    for i in range(N):
        for j in range(i+1, N):
            sort_list.append(A[i]*A[j])
    sort_list.sort()
    return sort_list
