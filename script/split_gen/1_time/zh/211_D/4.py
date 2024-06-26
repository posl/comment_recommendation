def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    now = 0
    for a, b in AB:
        if a > now:
            now = b - 1
            ans += 1
    print(ans)
