def main():
    cards = [int(x) for x in input().split()]
    print(sum(cards) - min(cards))
