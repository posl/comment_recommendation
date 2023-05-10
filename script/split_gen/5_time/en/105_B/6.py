def solve(N):
    for i in range(0, N//4 + 1):
        if (N - 4*i) % 7 == 0:
            return "Yes"
    return "No"
N = int(input())
print(solve(N))
