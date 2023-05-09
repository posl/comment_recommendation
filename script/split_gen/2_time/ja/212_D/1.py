def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    P = []
    X = []
    for i in range(Q):
        p, x = map(int, input().split())
        P.append(p)
        X.append(x)
    print(P)
    print(X)
