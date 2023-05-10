def triangles(n, l):
    ans = 0
    l.sort()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    ans += 1
    return ans
n = int(input())
l = list(map(int, input().split()))
ans = triangles(n, l)
print(ans)
