def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x:x[1])
    ans = 0
    pre = 0
    for ab in AB:
        if ab[0] > pre:
            ans += 1
            pre = ab[1] - 1
    print(ans)
