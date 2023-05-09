def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += (X[i] - X[N // 2]) ** 2
    print(ans)

if __name__ == '__main__':
    main()