def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    ng = d
    ok = M + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid ** len(X) <= M:
            ng = mid
        else:
            ok = mid
    print(ng - d)
