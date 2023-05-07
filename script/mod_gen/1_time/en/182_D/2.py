def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    now = 0
    for i in range(N):
        now += A[i]
        ans = max(ans, now)
    print(ans)

if __name__ == '__main__':
    main()