def find_even_sum(n, a):
    a.sort()
    max_even = -1
    for i in range(n-1):
        for j in range(i+1, n):
            if (a[i]+a[j])%2==0:
                max_even = max(max_even, a[i]+a[j])
            elif a[i]+a[j]>max_even:
                break
    return max_even
