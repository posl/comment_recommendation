def solve(n, s, cards):
    for i in range(0, 2 ** n):
        sum = 0
        for j in range(0, n):
            if (i >> j) & 1 == 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            return True, i
    return False, 0
n, s = map(int, input().split())
cards = []
for i in range(0, n):
    cards.append(list(map(int, input().split())))
result, i = solve(n, s, cards)
