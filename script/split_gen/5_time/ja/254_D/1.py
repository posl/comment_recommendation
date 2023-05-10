def solve():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j > N:
                break
            if (i * j) ** 0.5 == int((i * j) ** 0.5):
                ans += 1
    print(ans)
