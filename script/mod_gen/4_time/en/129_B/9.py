def solve(N,W):
    S1 = sum(W)
    S2 = 0
    for i in range(N):
        S2 += W[i]
        S1 -= W[i]
        if abs(S2-S1) < diff:
            diff = abs(S2-S1)
    return diff
N = int(input())
W = list(map(int,input().split()))
print(solve(N,W))

if __name__ == '__main__':
    solve()