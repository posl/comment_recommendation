def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    if len(cards) == len(set(cards)):
        print('Yes')
    else:
        print('No')
