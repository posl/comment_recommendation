def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    # print(AB)
    ans = 0
    end = 0
    for a, b in AB:
        if a > end:
            ans += 1
            end = b - 1
    print(ans)
