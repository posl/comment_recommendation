def triangle_count(n, l):
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
                    if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]:
                        count += 1
    return count
n = int(input())
l = list(map(int, input().split()))
print(triangle_count(n, l))
