def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    ans = 1
    bridge = ab[0][1]
    for i in range(m):
        if ab[i][0] > bridge:
            ans += 1
            bridge = ab[i][1]
    print(ans)

if __name__ == '__main__':
    main()