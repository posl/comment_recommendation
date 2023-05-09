def find_sum(n, s, cards):
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if (i & (1 << j)):
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if (sum == s):
            return i
    return -1

if __name__ == '__main__':
    find_sum()