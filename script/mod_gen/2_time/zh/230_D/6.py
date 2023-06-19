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
    i = 0
    j = 0
    ans = 0
    while i < N:
        if L[i] < R[j]:
            ans += 1
            i += 1
        else:
            ans -= 1
            j += 1
    print(ans)

if __name__ == '__main__':
    main()