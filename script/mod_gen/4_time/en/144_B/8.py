def solve(N):
    for i in range(1,10):
        if N % i == 0 and N / i < 10:
            return "Yes"
    return "No"

if __name__ == '__main__':
    solve()