def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            if X % 2 == 0:
                X = X // 2
        elif S[i] == 'L':
            X = 2 * X - 1
        elif S[i] == 'R':
            X = 2 * X + 1
    print(X)
