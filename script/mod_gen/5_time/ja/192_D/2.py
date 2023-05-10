def main():
    x = input()
    m = int(input())
    d = int(max(x))
    l = len(x)
    if l == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return
    def base_n_to_10(x, n):
        out = 0
        for i in range(1,len(str(x))+1):
            out += int(x[-i])*(n**(i-1))
        return out
    def is_ok(arg):
        if base_n_to_10(x, arg) <= m:
            return True
        else:
            return False
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    print(meguru_bisect(m+1, d+1)-d)

if __name__ == '__main__':
    main()