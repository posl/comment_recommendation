def solve(n, s, cards):
    if n == 1:
        if s == cards[0][0] or s == cards[0][1]:
            return True, [0]
        else:
            return False, []
    else:
        for i in range(2 ** n):
            bin_i = bin(i)[2:].zfill(n)
            sum = 0
            for j in range(n):
                if bin_i[j] == '0':
                    sum += cards[j][0]
                else:
                    sum += cards[j][1]
            if sum == s:
                return True, bin_i
        return False, []
n, s = map(int, input().split())
cards = []
for i in range(n):
    cards.append(list(map(int, input().split())))
res, bin_i = solve(n, s, cards)
