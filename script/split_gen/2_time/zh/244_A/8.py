def main():
    N, X = map(int, input().split())
    S = input()
    X -= 1
    for i in range(N):
        if S[i] == 'U':
            X //= 2
        elif S[i] == 'L':
            X = 2 * X + 1
        else:
            X = 2 * X + 2
    print(X + 1)
