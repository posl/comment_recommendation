def calc_dist(x, s, t):
    if x < s:
        return s - x
    elif t < x:
        return x - t
    else:
        return min(x - s, t - x) * 2 + max(x - s, t - x)
A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
for _ in range(Q):
    x = int(input())
    s = 0
    t = 0
    while s < A and S[s] < x:
        s += 1
    while t < B and T[t] < x:
        t += 1
    ans = float('inf')
    for Ss in [S[s - 1]] if s > 0 else [float('inf')] + [S[s]] if s < A else [float('inf')] * 2:
        for Tt in [T[t - 1]] if t > 0 else [float('inf')] + [T[t]] if t < B else [float('inf')] * 2:
            ans = min(ans, calc_dist(x, Ss, Tt))
    print(ans)

if __name__ == '__main__':
    calc_dist()