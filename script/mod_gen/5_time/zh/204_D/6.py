def solve(N, T):
    T.sort()
    T.reverse()
    oven1 = 0
    oven2 = 0
    for i in range(N):
        if oven1 < oven2:
            oven1 += T[i]
        else:
            oven2 += T[i]
    return max(oven1, oven2)

if __name__ == '__main__':
    solve()