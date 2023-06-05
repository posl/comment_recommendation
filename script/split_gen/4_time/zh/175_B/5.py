def triangle_number(n, a):
    a.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if a[i] + a[j] > a[k]:
                    count += 1
                else:
                    break
    return count
