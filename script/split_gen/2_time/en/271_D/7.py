def solve(n,s,ab):
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                sum += ab[j][0]
            else:
                sum += ab[j][1]
        if sum == s:
            return i
    return -1
