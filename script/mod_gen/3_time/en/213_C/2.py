def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

if __name__ == '__main__':
    main()