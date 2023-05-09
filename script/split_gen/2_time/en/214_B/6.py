def count(a, b, c):
    if a + b + c <= S and a * b * c <= T:
        return 1
    else:
        return 0
S, T = map(int, input().split())
ans = 0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            ans += count(a, b, c)
print(ans)
