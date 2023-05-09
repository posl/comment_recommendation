def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    bridge = [0] * (N + 1)
    for a, b in AB:
        if bridge[a] == 0:
            bridge[a] = 1
            bridge[b] = 1
            ans += 1
    print(M - ans)
main()

if __name__ == '__main__':
    main()