def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = 2 * X - 1
        else:
            X = 2 * X + 1
    print(X)
