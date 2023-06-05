def solve():
    n = int(input())
    card = set()
    for i in range(n):
        s = input()
        card.add(s)
    if len(card) == n:
        print('Yes')
    else:
        print('No')
solve()
