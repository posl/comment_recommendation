def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L = sorted(L)
    R = sorted(R)
    cnt = 0
    for i in range(N):
        if R[i] - L[i] + 1 < D:
            cnt += 1
        else:
            cnt += 2
    print(cnt)

if __name__ == '__main__':
    main()