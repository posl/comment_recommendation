def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'L':
            X = X * 2
        elif s == 'R':
            X = X * 2 + 1
        else:
            X = (X - 1) // 2
    print(X)
