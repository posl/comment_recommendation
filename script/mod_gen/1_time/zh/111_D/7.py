def get_pattern(x,y):
    if x < 0:
        return 'L',-x
    elif x == 0:
        if y > 0:
            return 'U',y
        else:
            return 'D',-y
    else:
        return 'R',x

if __name__ == '__main__':
    get_pattern()