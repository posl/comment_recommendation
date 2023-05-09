def permutation(arr, num):
    if num == 0:
        return [[]]
    else:
        return [[x] + y for x in arr for y in permutation(arr, num - 1) if x not in y]
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p in permutation(range(1, n), n - 1):
    time = 0
    p = [0] + p + [0]
    for i in range(n):
        time += t[p[i]][p[i + 1]]
    if time == k:
        ans += 1
print(ans)
