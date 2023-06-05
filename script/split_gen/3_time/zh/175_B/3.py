def solve(n, l):
    ans = 0
    l.sort()
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] + l[j] > l[k]:
                    ans += 1
    return ans
n = int(input())
l = list(map(int, input().split()))
print(solve(n, l))
