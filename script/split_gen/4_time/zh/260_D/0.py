def func(x, n, p):
    # x: number on the card
    # n: number of cards
    # p: permutation of the cards
    # return: the step that the card is eaten
    #print("func({},{},{})".format(x, n, p))
    #print("p[x-1]:{}".format(p[x-1]))
    if p[x-1] == 1:
        return 1
    else:
        return func(p[x-1], n, p) + 1
