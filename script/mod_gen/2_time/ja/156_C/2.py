def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, 101):
        tmp = 0
        for j in range(N):
            tmp += (X[j] - i)**2
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()