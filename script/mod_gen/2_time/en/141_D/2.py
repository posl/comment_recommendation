def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if M == 0:
            break
        if A[i] >= 2**M:
            break
        else:
            A[i] = A[i]//(2**(bin(A[i]).count("1")-1))
            M -= bin(A[i]).count("1")
    if M > 0:
        A[i] = A[i]//(2**M)
    print(sum(A))

if __name__ == '__main__':
    main()