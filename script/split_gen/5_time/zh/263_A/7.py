def main():
    cards = input()
    cards = cards.split(" ")
    cards = [int(i) for i in cards]
    cards.sort()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    elif cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")
