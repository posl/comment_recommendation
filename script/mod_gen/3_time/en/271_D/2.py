def main():
    N, S = [int(x) for x in input().split()]
    cards = []
    for i in range(N):
        cards.append([int(x) for x in input().split()])
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            print("Yes")
            for j in range(N):
                if (i >> j) & 1:
                    print("H",end="")
                else:
                    print("T",end="")
            print()
            return
    print("No")

if __name__ == '__main__':
    main()