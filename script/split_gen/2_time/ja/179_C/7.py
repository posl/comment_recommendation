def solve():
    N = int(input())
    ans = 0
    for i in range(1, N):
        for j in range(1, N):
            if i * j >= N:
                break
            if (N - i * j) % j == 0:
                ans += 1
    print(ans)
