def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if L[i] > R[j] or L[j] > R[i]:
                continue
            if R[i] - L[i] + R[j] - L[j] - D > 0:
                ans += 1
    print(ans)
    return
main()
