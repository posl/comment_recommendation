def get_coins(a,b):
    if a == b:
        return a*2
    elif a > b:
        return (a-1)*2
    else:
        return (b-1)*2

if __name__ == '__main__':
    get_coins()