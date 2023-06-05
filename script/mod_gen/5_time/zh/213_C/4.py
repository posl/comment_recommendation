def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    A.sort()
    B = list(set(B))
    B.sort()
    for i in range(N):
        a = A.index(A[i]) + 1
        b = B.index(B[i]) + 1
        print(a, b)

if __name__ == '__main__':
    main()