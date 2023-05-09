def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        print(1 if int(X) <= M else 0)
        return
    ok = d
    ng = 10 ** 18 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if int(X, mid) <= M:
            ok = mid
        else:
            ng = mid
    print(ok - d)

if __name__ == '__main__':
    main()