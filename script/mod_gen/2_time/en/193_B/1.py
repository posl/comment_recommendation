def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 1000000001
    for i in range(N):
        if X[i] > A[i]:
            min_price = min(min_price, P[i])
    if min_price == 1000000001:
        return -1
    else:
        return min_price
print(solve())

if __name__ == '__main__':
    solve()