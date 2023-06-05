def main():
    N,Q = map(int, input().split())
    A = [0]*(N+1)
    for i in range(N-1):
        a,b = map(int, input().split())
        A[a] += 1
        A[b] += 1
    for i in range(Q):
        p,x = map(int, input().split())
        A[p] += x
    print(' '.join(map(str, A[1:])))
