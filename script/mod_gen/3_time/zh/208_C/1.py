def problems208_c(n, k, a):
    if k >= n:
        return [k // n for i in range(n)]
    else:
        a = sorted(a)
        b = [0 for i in range(n)]
        for i in range(k):
            b[a[i]-1] += 1
        return b

if __name__ == '__main__':
    problems208_c()