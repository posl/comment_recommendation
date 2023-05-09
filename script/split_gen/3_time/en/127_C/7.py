def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    LR.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for l, r in LR:
        if l > last:
            ans += 1
            last = r
    print(ans)
