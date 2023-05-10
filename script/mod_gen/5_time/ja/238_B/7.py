def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    ans = 360 * N - ans
    print(ans)

if __name__ == '__main__':
    main()