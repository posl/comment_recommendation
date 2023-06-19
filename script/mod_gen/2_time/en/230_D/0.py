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
    ans = 0
    p = 0
    q = 0
    while p < N:
        if L[p] <= R[q]:
            p += 1
            ans += 1
        else:
            q += 1
            ans -= 1
    print(ans)
main()
