def get_permutation(s, k):
    if len(s) == 1:
        return s
    else:
        l = list(s)
        l.sort()
        s = ''.join(l)
        n = len(s)
        if k == 1:
            return s
        elif k == 2:
            return s[::-1]
        else:
            if k == factorial(n):
                return s[::-1]
            else:
                t = factorial(n-1)
                p = k / t
                q = k % t
                if q == 0:
                    q = t
                return s[p-1] + get_permutation(s[:p-1] + s[p:], q)
