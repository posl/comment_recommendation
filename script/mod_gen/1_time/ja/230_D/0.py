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
    for i in range(N):
        if L[i] + D - 1 < R[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()