def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    ans = []
    for i in range(Q):
        P, X = map(int, input().split())
        if P == 1:
            pass
        elif P == 2:
            pass
        else:
            ans.append(X)
    print('
'.join(map(str, ans)))
