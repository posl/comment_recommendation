def main():
    x = input()
    m = int(input())
    d = int(max(x))
    #print(d)
    def base_n(x, n):
        if (int(x / n)):
            return base_n(int(x / n), n) + str(x % n)
        return str(x % n)
    def is_ok(v):
        if m < int(v):
            return False
        return True
    def binary_search():
        ng = 0
        ok = 10**18
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(base_n(int(x), mid)):
                ng = mid
            else:
                ok = mid
        return ok
    print(binary_search() - d)
