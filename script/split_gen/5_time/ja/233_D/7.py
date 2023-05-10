def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    # print(s)
    l = 0
    r = 1
    ans = 0
    while l < N:
        # print(l, r, s[r] - s[l])
        if s[r] - s[l] == K:
            ans += 1
            l += 1
        elif s[r] - s[l] < K:
            r += 1
        else:
            l += 1
        if l == r:
            r += 1
    print(ans)
