def triangle_count(n, l):
    count = 0
    l.sort()
    for i in range(n-1, 1, -1):
        for j in range(i-1, 0, -1):
            for k in range(j-1, -1, -1):
                if l[i] < l[j] + l[k]:
                    count += 1
                else:
                    break
    return count
n = int(input())
l = list(map(int, input().split()))
print(triangle_count(n, l))
