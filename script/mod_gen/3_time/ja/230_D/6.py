def main():
    import sys
    input = sys.stdin.readline
    N, D = map(int, input().split())
    L = []
    R = []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    R.sort()
    L.sort()
    ans = 0
    for i in range(N):
        if L[i] + D - 1 >= R[i]:
            ans += 1
        else:
            j = bisect.bisect_left(R, L[i] + D)
            ans += N - j
    print(ans)

if __name__ == '__main__':
    main()