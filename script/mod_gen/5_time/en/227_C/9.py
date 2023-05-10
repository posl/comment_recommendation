def solve(N):
    count = 0
    for C in range(1, N + 1):
        for B in range(1, C + 1):
            A = N // (B * C)
            if A >= B:
                count += 1
            else:
                break
    return count

if __name__ == '__main__':
    solve()