def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += X
            K -= 1
        else:
            ans += A[i]
    if K > 0:
        ans += X * K
    print(ans)

if __name__ == '__main__':
    main()