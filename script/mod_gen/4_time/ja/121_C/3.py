def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if M == 0:
            break
        if b <= M:
            ans += a * b
            M -= b
        else:
            ans += a * M
            M = 0
    print(ans)

if __name__ == '__main__':
    main()