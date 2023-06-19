def solve():
    N, X = map(int, input().split())
    S = input()
    X -= 1
    for i in range(N):
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = X * 2
        else:
            X = X * 2 + 1
    print(X + 1)
