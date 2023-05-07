def calc_median(a, k, n):
    # a: 2d array
    # k: size of the subarray
    # n: size of the array
    ans = []
    for i in range(n-k+1):
        for j in range(n-k+1):
            sub_array = []
            for p in range(k):
                for q in range(k):
                    sub_array.append(a[i+p][j+q])
            sub_array.sort()
            ans.append(sub_array[(k*k)//2])
    return min(ans)
