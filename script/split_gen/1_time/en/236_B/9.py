def main():
    # Take in the number of cards
    n = int(input())
    # Take in the cards
    cards = list(map(int, input().split()))
    # Create a dictionary of the cards
    card_dict = {}
    for card in cards:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    # Find the card with the odd number of cards
    for key, value in card_dict.items():
        if value % 2 != 0:
            print(key)
            break
