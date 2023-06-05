def find_second_winner(n, players):
    """
    find the second winner in a tournament
    """
    if n == 1:
        return min(players[0], players[1])
    else:
        # find the winner in the first round
        winners = []
        for i in range(0, 2**n, 2):
            winners.append(max(players[i], players[i+1]))
        # find the second winner in the second round
        return find_second_winner(n-1, winners)

if __name__ == '__main__':
    find_second_winner()