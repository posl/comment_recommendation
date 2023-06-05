def judge(player1,player2):
    if player1 == player2:
        return 0
    elif player1 == 'G' and player2 == 'C':
        return 1
    elif player1 == 'C' and player2 == 'P':
        return 1
    elif player1 == 'P' and player2 == 'G':
        return 1
    else:
        return 2

if __name__ == '__main__':
    judge()