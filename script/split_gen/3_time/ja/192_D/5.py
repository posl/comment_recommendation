def main():
    X = input()
    M = int(input())
    d = max(map(int, X))
    if len(X) == 1:
        print(1 if d <= M else 0)
        return
    ok = d
    ng = 10 ** 18 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if int(X, mid) <= M:
            ok = mid
        else:
            ng = mid
    print(ok - d)
