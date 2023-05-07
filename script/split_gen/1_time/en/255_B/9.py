def main():
    import sys
    from math import sqrt
    def input(): return sys.stdin.readline().rstrip()
    def dist(x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)
    def check(x, y, r, n, k, a, X, Y):
        for i in range(n):
            if i+1 in a:
                if dist(x, y, X[i], Y[i]) > r:
                    return False
            else:
                if dist(x, y, X[i], Y[i]) <= r:
                    return False
        return True
    def solve(n, k, a, X, Y):
        ans = 10**10
        for i in range(n):
            for j in range(i+1, n):
                x = (X[i] + X[j]) / 2
                y = (Y[i] + Y[j]) / 2
                r = dist(x, y, X[i], Y[i])
                if check(x, y, r, n, k, a, X, Y):
                    ans = min(ans, r)
                for l in range(j+1, n):
                    x = (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j])) / \
                        (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j]))
                    y = (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j])) / \
                        (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j]))
                    r = dist(x, y, X[i], Y[i])
                    if check(x, y, r, n, k, a, X, Y):
                        ans = min(ans, r)
        return ans
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    print(solve
