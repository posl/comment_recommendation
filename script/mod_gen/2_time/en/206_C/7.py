def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += N - (i + 1)
        if i + 1 < N and A[i] == A[i + 1]:
            ans -= N - (i + 1)
            ans -= N - (i + 2)
    print(ans)

if __name__ == '__main__':
    main()