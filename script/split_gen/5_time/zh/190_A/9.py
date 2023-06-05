def game(a,b,c):
    if c == 0:
        if a > b:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if a >= b:
            return 'Takahashi'
        else:
            return 'Aoki'
