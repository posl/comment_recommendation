def solve(N, info):
    for i in range(101):
        for j in range(101):
            H = 0
            for k in range(N):
                if info[k][2] > 0:
                    H = info[k][2] + abs(i - info[k][0]) + abs(j - info[k][1])
                    break
            for k in range(N):
                if info[k][2] != max(H - abs(i - info[k][0]) - abs(j - info[k][1]), 0):
                    break
                if k == N - 1:
                    return [i, j, H]

if __name__ == '__main__':
    solve()