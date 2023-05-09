def main():
    n, w = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(n):
        a, b = ab[i]
        ans += a * min(b, w)
        w -= min(b, w)
        if w == 0:
            print(ans)
            exit()

if __name__ == '__main__':
    main()