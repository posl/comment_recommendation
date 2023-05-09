def main():
    # input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # compute
    cnt = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) >= K:
                cnt += 1
    # output
    print(cnt)

if __name__ == '__main__':
    main()