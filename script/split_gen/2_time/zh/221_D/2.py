def f(N):
    if N < 10:
        return 0
    elif N < 20:
        return N - 10
    else:
        return (N - 10) * (N - 10)
N = int(input())
ans = 0
for i in range(1, N):
    ans = max(ans, f(i) * f(N - i))
print(ans)
