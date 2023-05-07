def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                ans += A[i] * A[j]
    print(ans % mod)

if __name__ == '__main__':
    main()