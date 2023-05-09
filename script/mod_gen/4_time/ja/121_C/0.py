def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(M)
    result = 0
    for i in range(N):
        if M > 0:
            if M >= B[i]:
                result += A[i] * B[i]
                M -= B[i]
            else:
                result += A[i] * M
                M = 0
        else:
            break
    print(result)

if __name__ == '__main__':
    main()