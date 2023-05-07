def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    l = 0
    r = 10**10
    while r-l > 10**(-5):
        m = (l+r)/2
        if check(N, K, A, X, Y, m):
            r = m
        else:
            l = m
    print(r)
