def solve():
    n, m = map(int, input().split())
    cards = [0] * (n + 1)
    for i in range(m):
        l, r = map(int, input().split())
        cards[l - 1] += 1
        cards[r] -= 1
    for i in range(1, n + 1):
        cards[i] += cards[i - 1]
    return cards.count(m)
print(solve())
