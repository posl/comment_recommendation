def main():
    N, K = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    A.append(10**100)
    B.append(0)
    p = 0
    for i in range(N):
        if K < A[i]:
            break
        p = B[i]
    print(K + p)

if __name__ == '__main__':
    main()