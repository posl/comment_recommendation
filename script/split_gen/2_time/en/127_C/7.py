def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    LR.sort(key=lambda x: x[1])
    ans = 0
    right = 0
    for L, R in LR:
        if right < L:
            ans += 1
            right = R
    print(ans)
