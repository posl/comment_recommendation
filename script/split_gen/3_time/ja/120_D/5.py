def main():
    import sys
    readline = sys.stdin.readline
    from collections import defaultdict
    N, M = map(int, readline().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, readline().split())
    A.reverse()
    B.reverse()
    #print(A)
    #print(B)
    d = defaultdict(int)
    for i in range(1, N+1):
        d[i] = 1
    #print(d)
    ans = [0]*M
    for i in range(M):
        ans[M-i-1] = (N*(N-1))//2 - (N-d[A[i]])*(N-d[B[i]])
        d[A[i]] += 1
        d[B[i]] += 1
    for i in range(M):
        print(ans[i])
