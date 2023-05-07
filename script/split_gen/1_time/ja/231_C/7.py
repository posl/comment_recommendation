def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for i in range(Q)]
    A.sort()
    for i in range(Q):
        l,r = 0,N
        while r-l > 1:
            m = (r+l)//2
            if A[m] > x[i]:
                r = m
            else:
                l = m
        print(N-r)
