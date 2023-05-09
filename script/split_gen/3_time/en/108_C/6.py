def get_ints():
    return map(int, input().split())
N, K = get_ints()
ans = 0
for i in range(1, N + 1):
    if i % K == 0:
        ans += 1
print(ans**3)
