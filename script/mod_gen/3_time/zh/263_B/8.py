def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = max(ans, dfs(i, P))
    print(ans)

if __name__ == '__main__':
    main()