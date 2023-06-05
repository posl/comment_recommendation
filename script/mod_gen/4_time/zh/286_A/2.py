def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = []
    for i in range(N):
        B.append(A[i])
    for i in range(N):
        if i < P-1 or i > S-1:
            print(B[i],end=' ')
        elif i >= P-1 and i < Q-1:
            print(B[i+R-Q],end=' ')
        elif i >= Q-1 and i < R-1:
            print(B[i+P-Q],end=' ')
        else:
            print(B[i+S-R],end=' ')

if __name__ == '__main__':
    main()