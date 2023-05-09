def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for i in range(Q)]
    B = [0]*N
    for i in range(N):
        B[i] = A[i]-i-1
    B.sort()
    for i in range(Q):
        if X[i] > B[N-1]:
            print(B[N-1]+i+1)
        elif X[i] < B[0]:
            print(B[0]-i-1)
        else:
            l = 0
            r = N-1
            while r-l>1:
                m = (l+r)//2
                if B[m] < X[i]:
                    l = m
                else:
                    r = m
            print(X[i]+l+1)

if __name__ == '__main__':
    main()