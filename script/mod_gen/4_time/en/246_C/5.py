def main():
    N, K, X = map(int, input().split())
    A = [int(n) for n in input().split()]
    ans = 0
    for i in range(N):
        ans += max(A[i] - K*X, 0)
    print(ans)

if __name__ == '__main__':
    main()