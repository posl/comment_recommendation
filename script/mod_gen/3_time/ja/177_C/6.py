def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 10**9+7
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A[i] * A[j]
    print(ans % P)

if __name__ == '__main__':
    main()