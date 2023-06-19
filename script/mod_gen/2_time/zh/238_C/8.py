def calc(N):
    if N < 10:
        return N
    else:
        s = str(N)
        l = len(s)
        first = int(s[0])
        if first == 1:
            return calc(10 ** (l - 1) - 1) + calc(N - 10 ** (l - 1))
        else:
            return first * calc(10 ** (l - 1) - 1) + calc(N - first * (10 ** (l - 1)))
N = int(input())
print(calc(N) % 998244353)
