def cardgame(n, s, cards):
    for i in range(2**n):
        sum = 0
        result = ""
        for j in range(n):
            if (i >> j) & 1:
                sum += cards[j][0]
                result += "H"
            else:
                sum += cards[j][1]
                result += "T"
        if sum == s:
            return "Yes", result
    return "No", ""

if __name__ == '__main__':
    cardgame()