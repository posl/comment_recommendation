def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    X, Y = zip(*XY)
    if sum([X[i] == X[i + 1] and Y[i] == Y[i + 1] for i in range(N - 1)]) == N - 1:
        print(-1)
        return
    for m in range(1, 41):
        for d in range(1, 10 ** 12 + 1):
            if m * d < max(abs(max(X)), abs(max(Y))):
                continue
            if m * d < max(abs(min(X)), abs(min(Y))):
                continue
            if m * d > max(abs(max(X)), abs(max(Y))):
                continue
            if m * d > max(abs(min(X)), abs(min(Y))):
                continue
            if m * d > max(abs(max(X)), abs(max(Y))):
                continue
            if m * d > max(abs(min(X)), abs(min(Y))):
                continue
            break
        else:
            continue
        break
    else:
        print(-1)
        return
    print(m)
    print(*[d] * m)
    for x, y in XY:
        ans = []
        for i in range(m):
            if x < 0:
                ans.append('L')
                x += d
            else:
                ans.append('R')
                x -= d
        for i in range(m):
            if y < 0:
                ans.append('D')
                y += d
            else:
                ans.append('U')
                y -= d
        print(*ans, sep='')

if __name__ == '__main__':
    solve()