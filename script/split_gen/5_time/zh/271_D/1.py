def solve(n,s,card):
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if ((i >> j) & 1):
                sum += card[j][0]
            else:
                sum += card[j][1]
        if sum == s:
            return True,i
    return False,0
