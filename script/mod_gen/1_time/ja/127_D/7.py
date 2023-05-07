def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        B.append(list(map(int, input().split())))
    for i in range(M):
        C.append(B[i][1])
    C.sort(reverse=True)
    A.sort(reverse=True)
    count = 0
    for i in range(N):
        if count < M:
            if A[i] < C[count]:
                A[i] = C[count]
                count += 1
    print(sum(A))

if __name__ == '__main__':
    main()