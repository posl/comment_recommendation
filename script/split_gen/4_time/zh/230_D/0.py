def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    l = 0
    r = 0
    ans = 0
    while l < N:
        if L[l] <= R[r]:
            l += 1
            ans = max(ans, l - r)
        else:
            r += 1
    print(ans)
