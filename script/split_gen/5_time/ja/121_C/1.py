def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if M <= b:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    print(ans)
main()
