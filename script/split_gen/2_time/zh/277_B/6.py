def main():
    n = int(input())
    card = []
    for i in range(n):
        card.append(input())
    if len(card) != len(set(card)):
        print('No')
    else:
        flag = True
        for i in card:
            if i[0] not in ['H', 'D', 'C', 'S']:
                flag = False
                break
            elif i[1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T','J', 'Q', 'K']:
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
