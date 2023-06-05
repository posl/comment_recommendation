def check(card):
    #print(card)
    if card[0] in 'HDCS' and card[1] in 'A23456789TJQK':
        return True
    else:
        return False
n = int(input())
cards = []
for i in range(n):
    cards.append(input())
#print(cards)
cards.sort()
#print(cards)
for i in range(n-1):
    if cards[i] == cards[i+1]:
        print('No')
        exit()
for card in cards:
    if check(card) == False:
        print('No')
        exit()
print('Yes')
