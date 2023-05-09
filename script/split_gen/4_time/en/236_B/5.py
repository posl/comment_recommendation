def main():
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    if n % 2 == 0:
        if cards[0] != cards[1]:
            print(0)
            return
        if cards[-1] != cards[-2]:
            print(0)
            return
        for i in range(1, n):
            if cards[2 * i - 1] != cards[2 * i]:
                print(0)
                return
        print(pow(2, n // 2, 1000000007))
        return
    else:
        if cards[0] != cards[1]:
            print(0)
            return
        if cards[-1] != cards[-2]:
            print(0)
            return
        for i in range(1, n):
            if cards[2 * i - 1] != cards[2 * i]:
                print(0)
                return
        print(pow(2, n // 2, 1000000007))
        return
