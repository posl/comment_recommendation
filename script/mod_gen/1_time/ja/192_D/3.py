def main():
    X = input()
    M = int(input())
    N = len(X)
    d = int(max(X))
    if N == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    ok = d
    ng = M + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        s = 0
        for i in range(N):
            s = s * mid + int(X[i])
            if s > M:
                break
        if s <= M:
            ok = mid
        else:
            ng = mid
    print(ok - d)

if __name__ == '__main__':
    main()