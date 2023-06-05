def main():
    N,M,Q = map(int,input().split())
    l = [0] * (N + 1)
    r = [0] * (N + 1)
    for i in range(M):
        a,b = map(int,input().split())
        l[a] += 1
        r[b] += 1
    for i in range(1,N+1):
        l[i] += l[i-1]
        r[i] += r[i-1]
    for i in range(Q):
        p,q = map(int,input().split())
        print(r[q] - l[p-1])
