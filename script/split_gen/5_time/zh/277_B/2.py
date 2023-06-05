def judge():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    cards.sort()
    for i in range(n-1):
        if cards[i] == cards[i+1]:
            return "No"
    return "Yes"
print(judge())
