def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        cnt = 0
        for a in A:
            if a & (1 << i):
                cnt += 1
        if cnt * 2 < N:
            ans += 1 << i
        if ans + (1 << i) - 1 <= K:
            ans += 1 << i
    print(ans)
