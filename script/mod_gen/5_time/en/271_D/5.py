def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    print(cards)
    for i in range(2**n):
        ans = []
        for j in range(n):
            if i & (1 << j):
                ans.append(cards[j][0])
            else:
                ans.append(cards[j][1])
        print(ans)
        if sum(ans) == s:
            print("Yes")
            print(ans)
            return
    print("No")

if __name__ == '__main__':
    main()