def main():
    X = input()
    M = int(input())
    d = max([int(X[i]) for i in range(len(X))])
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    def is_ok(n):
        ans = 0
        for i in range(len(X)):
            ans += int(X[i]) * (n ** (len(X) - i - 1))
        return ans <= M
    def meguru_bisect(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    print(meguru_bisect(d, M + 1) - d)

if __name__ == '__main__':
    main()