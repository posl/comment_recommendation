def main():
    n = int(input())
    card = []
    for i in range(n):
        card.append(input())
    if len(set(card)) != n:
        print("No")
        return
    for i in range(n):
        if card[i][0] not in "HDCS":
            print("No")
            return
    for i in range(n):
        if card[i][1] not in "A23456789TJQK":
            print("No")
            return
    print("Yes")
