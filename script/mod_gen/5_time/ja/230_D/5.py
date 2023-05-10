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
    L = L[::-1]
    R = R[::-1]
    ans = 0
    l = 0
    r = 0
    while l < N and r < N:
        if L[l] <= R[r]:
            ans += 1
            l += 1
        else:
            ans -= 1
            r += 1
    print(ans)

if __name__ == '__main__':
    main()