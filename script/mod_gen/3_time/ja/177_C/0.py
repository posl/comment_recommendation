def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += A[i] * A[j]
    print(ans % (10**9+7))

if __name__ == '__main__':
    main()