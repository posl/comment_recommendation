def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 1000000000
    for i in range(N):
        if X[i] > 0 and ans > P[i]:
            ans = P[i]
    if ans == 1000000000:
        ans = -1
    print(ans)
