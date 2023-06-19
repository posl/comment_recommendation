def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += t[0][i]
    print(ans)

if __name__ == '__main__':
    main()