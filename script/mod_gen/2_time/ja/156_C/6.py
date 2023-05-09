def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += (X[i] - X[i // 2]) ** 2
    print(ans)

if __name__ == '__main__':
    main()