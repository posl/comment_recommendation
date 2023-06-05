def get_max_number(n, m, a):
    a.sort(reverse=True)
    # print(a)
    # print(n, m)
    result = ''
    while n > 0:
        for i in range(m):
            if a[i] <= n:
                result += str(a[i])
                n -= a[i]
                break
    return result
