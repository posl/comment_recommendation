def main():
    N, K = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    for i in range(N):
        if K >= A[i]:
            K += B[i]
        else:
            print(K)
            return
    print(K)

if __name__ == '__main__':
    main()