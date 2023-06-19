def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    if sorted(A) == A:
        print("Yes")
    else:
        for i in range(N-K):
            if A[i] > A[i+K]:
                A[i],A[i+K] = A[i+K],A[i]
        if sorted(A) == A:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()