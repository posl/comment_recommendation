def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    ans = N*M - sum
    if ans > K:
        print(-1)
    else:
        print(max(ans, 0))

if __name__ == '__main__':
    main()