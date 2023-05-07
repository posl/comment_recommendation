def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K-1, -1, -1):
        if N == 0:
            break
        if N >= A[i]:
            ans += A[i] * (N // A[i])
            N %= A[i]
    print(ans)

if __name__ == '__main__':
    main()