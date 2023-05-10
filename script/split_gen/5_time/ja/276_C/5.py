def getPermutation(n, k, p):
    ans = [0] * n
    used = [False] * n
    for i in range(n):
        for j in range(n):
            if used[j]:
                continue
            if p[i] == j + 1:
                used[j] = True
                ans[i] = j + 1
                break
    return ans
n = int(input())
p = list(map(int, input().split()))
k = 1
for i in range(n):
    k += math.factorial(n - i - 1) * (p[i] - sum([1 if p[i] > p[j] else 0 for j in range(i)]))
ans = getPermutation(n, k, p)
print(' '.join(map(str, ans)))
