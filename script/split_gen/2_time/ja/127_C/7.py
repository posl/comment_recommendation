def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    L = [0 for _ in range(N)]
    R = [0 for _ in range(N)]
    for i in range(1, N+1):
        for l, r in LR:
            if l == i:
                L[i-1] += 1
            if r == i:
                R[i-1] += 1
    ans = 0
    for i in range(N):
        if L[i] == 1 and R[i] == 1:
            ans += 1
    print(ans)
