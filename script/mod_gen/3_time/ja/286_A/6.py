def main():
    N,P,Q,R,S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A.copy()
    for i in range(N):
        if i+1 >= P and i+1 <= Q:
            B[i] = A[i+(S-R)]
        elif i+1 >= R and i+1 <= S:
            B[i] = A[i-(S-R)]
    print(*B)

if __name__ == '__main__':
    main()