def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for i in range(M):
        if ab[i][0] > bridge:
            ans += 1
            bridge = ab[i][1] - 1
    print(ans)

if __name__ == '__main__':
    main()