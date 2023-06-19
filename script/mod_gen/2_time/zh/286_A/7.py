def main():
    N,P,Q,R,S = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if i >= P-1 and i <= Q-1:
            B.append(A[i+R-Q])
        elif i >= R-1 and i <= S-1:
            B.append(A[i+P-R])
        else:
            B.append(A[i])
    for i in range(N):
        print(B[i], end = ' ')

if __name__ == '__main__':
    main()