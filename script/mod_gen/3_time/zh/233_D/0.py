def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, K)
    # print(A)
    # print(len(A))
    count = 0
    for i in range(N):
        for j in range(i+1,N+1):
            # print(i,j)
            # print(A[i:j])
            if sum(A[i:j]) == K:
                count += 1
    print(count)

if __name__ == '__main__':
    main()