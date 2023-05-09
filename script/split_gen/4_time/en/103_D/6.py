def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    right = 0
    for a, b in AB:
        if right < a:
            right = b - 1
            ans += 1
    print(ans)
