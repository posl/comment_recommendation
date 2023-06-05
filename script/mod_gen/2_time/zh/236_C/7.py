def solve():
    N = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    for i in range(0, len(cards), 4):
        if len(set(cards[i:i+4])) != 1:
            print(cards[i])
            break

if __name__ == '__main__':
    solve()