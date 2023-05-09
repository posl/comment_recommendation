def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            print("Yes")
            for j in range(n):
                if (i >> j) & 1 == 1:
                    print("H", end="")
                else:
                    print("T", end="")
            print("")
            return
    print("No")
    return

if __name__ == '__main__':
    main()