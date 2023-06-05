def isFullHouse(a,b,c,d,e):
    if a==b and a==c and d==e:
        return True
    elif a==b and c==d and c==e:
        return True
    else:
        return False

if __name__ == '__main__':
    isFullHouse()