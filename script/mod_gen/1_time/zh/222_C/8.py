def isWin(player1, player2):
    if player1 == 'G' and player2 == 'C':
        return True
    elif player1 == 'C' and player2 == 'P':
        return True
    elif player1 == 'P' and player2 == 'G':
        return True
    else:
        return False

if __name__ == '__main__':
    isWin()