def main():
    N = int(input())
    A = [0]*N
    P = [0]*N
    X = [0]*N
    for i in range(N):
        A[i], P[i], X[i] = map(int, input().split())
    minp = 10**9+1
    for i in range(N):
        if X[i]-A[i] > 0:
            minp = min(minp, P[i])
    if minp == 10**9+1:
        print(-1)
    else:
        print(minp)
main()
