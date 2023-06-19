def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    p = list(range(1, N+1))
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M):
        if A[i] == p[0] and B[i] == p[1]:
            p[0], p[1] = p[1], p[0]
            break
    for i in range(2, N):
        for j in range(M):
            if A[j] == p[i]:
                if B[j] == p[i-1]:
                    p[i-1], p[i] = p[i], p[i-1]
                    break
                elif B[j] == p[i-2]:
                    p[i-2], p[i-1] = p[i-1], p[i-2]
                    p[i-1], p[i] = p[i], p[i-1]
                    break
    print(*p)

if __name__ == '__main__':
    main()