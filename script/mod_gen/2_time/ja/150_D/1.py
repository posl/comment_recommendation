def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += (M // A[i]) * (A[i] // 2)
    print(ans)

if __name__ == '__main__':
    main()