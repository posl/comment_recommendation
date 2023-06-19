def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A[0:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    for i in range(N):
        if i == N-1:
            print(B[i])
        else:
            print(B[i],end=' ')

if __name__ == '__main__':
    main()