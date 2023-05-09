def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= X:
            ans += A[i]
        else:
            ans += X
    ans -= K * X
    if ans < 0:
        ans = 0
    print(ans)

if __name__ == '__main__':
    main()