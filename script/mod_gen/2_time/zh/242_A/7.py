def func(a,b,c,x):
    if x <= a:
        return 1
    elif x > b:
        return 0
    else:
        return c/(b-a)

if __name__ == '__main__':
    func()