def main():
    X = input()
    M = int(input())
    l = len(X)
    d = int(max(X))
    if l == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
    else:
        def digit(n):
            if n < 10:
                return 1
            else:
                return 1 + digit(n//10)
        def convert(n, d):
            l = digit(n)
            s = 0
            for i in range(l):
                s += n%10 * pow(d, i)
                n //= 10
            return s
        def check(n):
            if convert(n, d+1) <= M:
                return True
            else:
                return False
        def binary_search():
            ok = M+1
            ng = 0
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if check(mid):
                    ng = mid
                else:
                    ok = mid
            return ok - M
        print(binary_search())
