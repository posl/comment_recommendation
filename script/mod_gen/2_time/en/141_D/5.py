def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        print(A[i])
        for j in range(M):
            if A[i] >= A[i+1]:
                A[i] = A[i]/(2**(j+1))
            else:
                A[i] = A[i]/(2**(j))
    print(A)

if __name__ == '__main__':
    main()