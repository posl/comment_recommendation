def solve():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = X // 2
        elif s == 'L':
            X = 2 * X - 1
        else:
            X = 2 * X + 1
    print(X)
