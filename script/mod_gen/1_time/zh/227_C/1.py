def solve(N):
    cnt = 0
    for i in range(1, int(N ** (1.0 / 3)) + 1):
        for j in range(i, int((N - i ** 3) ** (1.0 / 2)) + 1):
            cnt += int((N - i ** 3 - j ** 3) ** (1.0 / 2)) - j
    return cnt
N = int(input())
print(solve(N))
