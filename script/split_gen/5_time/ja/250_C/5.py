def main():
    N,Q = map(int,input().split())
    x = [int(input()) for _ in range(Q)]
    L = list(range(1,N+1))
    for i in range(Q):
        L[x[i]-1],L[x[i]] = L[x[i]],L[x[i]-1]
    print(*L)
