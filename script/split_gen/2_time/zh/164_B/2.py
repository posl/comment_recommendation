def battle(a,b,c,d):
    while True:
        c = c - b
        if c <= 0:
            return 'Yes'
        a = a - d
        if a <= 0:
            return 'No'
