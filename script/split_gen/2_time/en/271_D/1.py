def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        a, b = map(int, input().split())
        cards.append([a, b])
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if (i>>j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            print("Yes")
            for j in range(n):
                if (i>>j) & 1:
                    print("T", end="")
                else:
                    print("H", end="")
            print("")
            return
    print("No")
    return
