def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if b <= M:
            ans += a * b
            M -= b
        else:
            ans += a * M
            break
    print(ans)
