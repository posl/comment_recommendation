def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    r = AB[0][1]
    for a, b in AB:
        if a <= r:
            continue
        ans += 1
        r = b
    print(ans)
