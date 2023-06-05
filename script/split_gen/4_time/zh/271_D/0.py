def main():
    n, s = map(int, input().split())
    cards = []
    for _ in range(n):
        a, b = map(int, input().split())
        cards.append((a, b))
    # print(cards)
    # print(n, s)
    for i in range(2 ** n):
        # print(i)
        total = 0
        for j in range(n):
            if (i >> j) & 1:
                total += cards[j][0]
            else:
                total += cards[j][1]
        if total == s:
            print("Yes")
            for j in range(n):
                if (i >> j) & 1:
                    print("H", end="")
                else:
                    print("T", end="")
            print()
            return
    print("No")
