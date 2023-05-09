def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.insert(0, 0)
    A.append(N + 1)
    B = []
    for i in range(M + 1):
        if A[i + 1] - A[i] - 1 > 0:
            B.append(A[i + 1] - A[i] - 1)
    if len(B) == 0:
        print(0)
        return
    K = min(B)
    for i in range(len(B)):
        if B[i] % K == 0:
            B[i] = B[i] // K
        else:
            B[i] = B[i] // K + 1
    print(sum(B))

if __name__ == '__main__':
    main()