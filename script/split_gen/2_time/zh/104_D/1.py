def solve(s):
    modulo = 10**9 + 7
    q = s.count('?')
    if q == 0:
        return countABC(s)
    res = 0
    for i in range(3**q):
        res += countABC(s.replace('?', 'A', i))
        res %= modulo
    return res
