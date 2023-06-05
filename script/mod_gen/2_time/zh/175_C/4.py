def triangle_count(n, l):
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    count += 1
                elif l[k] >= l[i] + l[j]:
                    break
    return count

if __name__ == '__main__':
    triangle_count()