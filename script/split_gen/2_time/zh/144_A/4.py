def triangle(n,l):
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i] + l[j] > l[k]:
                    count += 1
    return count
