def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    cnt = 0
    bridge = 0
    for i in range(m):
        if ab[i][0] > bridge:
            cnt += 1
            bridge = ab[i][1] - 1
    print(cnt)

if __name__ == '__main__':
    main()