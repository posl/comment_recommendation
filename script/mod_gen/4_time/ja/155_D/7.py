def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a for a in A if a < 0]
    B = list(reversed(A))
    C = []
    D = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            C.append(A[i] * A[j])
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            D.append(B[i] * B[j])
    E = C + D
    E.sort()
    print(E[K - 1])

if __name__ == '__main__':
    main()