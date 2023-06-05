def main():
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    for i in range(0, 4*n-1, 2):
        if cards[i] != cards[i+1]:
            print(cards[i])
            break
