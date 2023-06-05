def find_second_player(n, a):
    # find the second player in the final game
    # n: number of players
    # a: list of the players' scores
    # return: the second player's id
    # 2^n players, a list of 2^n scores
    # a[1] is the winner
    # a[2] is the second player
    # a[2^n] is the loser
    # a[2^n-1] is the second loser
    # a[2^n-2] is the third loser
    # a[2^n-3] is the fourth loser
    # a[2^n-4] is the fifth loser
    # ...
    # a[2^n-2^(n-1)] is the first loser
    # a[2^n-2^(n-1)+1] is the second player
    # a[2^n-2^(n-1)+2] is the third player
    # ...
    # a[2^n-2^(n-2)] is the last player
    # a[2^n-2^(n-2)+1] is the first player
    # a[2^n-2^(n-2)+2] is the second player
    # ...
    # a[2^n-2^(n-3)] is the last player
    # a[2^n-2^(n-3)+1] is the first player
    # ...
    # a[2^n-2^(n-4)] is the last player
    # a[2^n-2^(n-4)+1] is the first player
    # ...
    # a[2^n-2^(n-5)] is the last player
    # a[2^n-2^(n-5)+1] is the first player
    # ...
    # a[2^n-2^(n-6)] is the last player
    # a[2^n-2^(n-6)+1] is the first player
    # ...
    # a[2^n-2^(n-7)] is the last player
    # a[2^n-2^(n-7)+1] is the first player
    # ...
    # a[2^n-2^(n-8)] is the last player
    #

if __name__ == '__main__':
    find_second_player()