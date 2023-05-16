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
    ans = N
    i = 0
    j = 0
    while i < N:
        if L[i] - R[j] > D:
            ans -= 1
            j += 1
        else:
            i += 1
    print(ans)

if __name__ == '__main__':
    main()