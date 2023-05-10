def calc(n, k, a):
    if n >= k:
        return [1 for i in range(n)]
    else:
        k = k % n
        a.sort()
        result = [0 for i in range(n)]
        for i in range(k):
            result[a[i][1]] += 1
        return result

if __name__ == '__main__':
    calc()