def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if M <= b:
            ans += a * M
            break
        else:
            M -= b
            ans += a * b
    print(ans)

if __name__ == '__main__':
    main()