def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(M):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for ab in AB:
        if ab[0] > bridge:
            bridge = ab[1] - 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()