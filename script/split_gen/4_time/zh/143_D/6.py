def count_triangle(n, l):
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
                else:
                    break
    return count
