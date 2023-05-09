def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if b >= M:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    print(ans)

if __name__ == '__main__':
    main()