def solve(N):
    if N == 1:
        return 2
    elif N == 2:
        return 3
    else:
        N = N * 2
        i = 1
        while i * i <= N:
            if N % i == 0:
                if (N // i - i + 1) % 2 == 0:
                    return (N // i - i + 1) // 2
            i += 1
N = int(input())
print(solve(N))
