def main():
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    if S.count('L') > 0 and S.count('R') > 0:
        print('Yes')
    else:
        print('No')
