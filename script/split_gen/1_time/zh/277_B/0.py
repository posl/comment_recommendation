def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    cards.sort()
    for i in range(n-1):
        if cards[i] == cards[i+1]:
            print('No')
            return
    print('Yes')
