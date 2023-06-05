def solve(n, s, cards):
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            return True, i
    return False, 0

if __name__ == '__main__':
    solve()