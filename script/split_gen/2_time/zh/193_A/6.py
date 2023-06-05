def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
    else:
        def base_n_to_10(X, n):
            out = 0
            for i in range(1, len(X) + 1):
                out += int(X[-i]) * (n ** (i - 1))
            return out
        def base_10_to_n(x, n):
            out = ''
            while x > 0:
                out = str(x % n) + out
                x //= n
            return out
        def solve(X, M, d):
            if base_n_to_10(X, d + 1) > M:
                return 0
            else:
                n = d + 1
                while base_n_to_10(X, n) <= M:
                    n += 1
                return n - d - 1
        print(solve(X, M, d))
