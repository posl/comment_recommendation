def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    X.sort()
    Y.sort()
    x = X[N//2]
    y = Y[N//2]
    if N % 2 == 0:
        x = (x + X[N//2 - 1]) / 2
        y = (y + Y[N//2 - 1]) / 2
    for s in S:
        if s == 'U':
            y += 1
        elif s == 'D':
            y -= 1
        elif s == 'R':
            x += 1
        elif s == 'L':
            x -= 1
        else:
            assert False
    if N % 2 == 0:
        if x == int(x) and y == int(y):
            print('Yes')
        else:
            print('No')
    else:
        if x == X[N//2] and y == Y[N//2]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()