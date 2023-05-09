def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    L = [0] + L
    R = [0] + R
    l = 1
    r = 1
    ans = N
    while l <= N and r <= N:
        if L[l] + D - 1 < R[r]:
            l += 1
        else:
            ans = min(ans, N - (l - 1) + (r - 1))
            r += 1
    print(ans)
