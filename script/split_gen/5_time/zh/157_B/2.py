def bingo():
    bingoCard = []
    for i in range(3):
        bingoCard.append(input().split())
    N = int(input())
    b = []
    for i in range(N):
        b.append(input())
    for i in range(3):
        for j in range(3):
            if bingoCard[i][j] in b:
                bingoCard[i][j] = 0
    if bingoCard[0][0] == 0 and bingoCard[0][1] == 0 and bingoCard[0][2] == 0:
        return 'Yes'
    elif bingoCard[1][0] == 0 and bingoCard[1][1] == 0 and bingoCard[1][2] == 0:
        return 'Yes'
    elif bingoCard[2][0] == 0 and bingoCard[2][1] == 0 and bingoCard[2][2] == 0:
        return 'Yes'
    elif bingoCard[0][0] == 0 and bingoCard[1][0] == 0 and bingoCard[2][0] == 0:
        return 'Yes'
    elif bingoCard[0][1] == 0 and bingoCard[1][1] == 0 and bingoCard[2][1] == 0:
        return 'Yes'
    elif bingoCard[0][2] == 0 and bingoCard[1][2] == 0 and bingoCard[2][2] == 0:
        return 'Yes'
    elif bingoCard[0][0] == 0 and bingoCard[1][1] == 0 and bingoCard[2][2] == 0:
        return 'Yes'
    elif bingoCard[0][2] == 0 and bingoCard[1][1] == 0 and bingoCard[2][0] == 0:
        return 'Yes'
    else:
        return 'No'
print(bingo())
