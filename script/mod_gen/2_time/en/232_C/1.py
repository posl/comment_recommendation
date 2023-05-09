def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(M):
                if A[k] == i + 1 and B[k] == j + 1:
                    a = k
                if A[k] == j + 1 and B[k] == i + 1:
                    b = k
            for k in range(M):
                if C[k] == i + 1 and D[k] == j + 1:
                    c = k
                if C[k] == j + 1 and D[k] == i + 1:
                    d = k
            if (a == c and b == d) or (a == d and b == c):
                continue
            else:
                print("No")
                return
    print("Yes")
    return
main()

if __name__ == '__main__':
    main()