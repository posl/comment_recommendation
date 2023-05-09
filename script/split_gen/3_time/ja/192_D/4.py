def main():
    X = input()
    M = int(input())
    d = max(X)
    d = int(d)
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    ng = 0
    ok = M + 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if mid ** len(X) <= M:
            ng = mid
        else:
            ok = mid
    if d + 1 <= ok:
        print(ok - d - 1)
    else:
        print(0)
