def solution(n, a):
    a.sort()
    if a[0] == 0:
        return -1
    elif a[-1] % 2 == 0:
        return a[-1]
    else:
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (a[i] + a[j]) % 2 == 0:
                    return a[i] + a[j]
        return -1
