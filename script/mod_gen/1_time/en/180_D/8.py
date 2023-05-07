def max_exp(x,y,a,b):
    exp = 0
    str = x
    while True:
        if str >= y:
            break
        if str*a < str+b:
            str = str*a
            exp = exp+1
        else:
            str = str+b
            exp = exp+1
    return exp-1

if __name__ == '__main__':
    max_exp()