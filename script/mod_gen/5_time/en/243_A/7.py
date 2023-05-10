def func(v,a,b,c):
    if v <= a:
        return 'F'
    elif v <= a+b:
        return 'M'
    elif v <= a+b+c:
        return 'T'
    else:
        return None

if __name__ == '__main__':
    func()