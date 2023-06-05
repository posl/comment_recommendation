def round(x):
    if x.isdecimal():
        return x
    else:
        if '.' in x:
            x = x.split('.')
            if x[1][0] >= '5':
                x[0] = str(int(x[0]) + 1)
            return x[0]
        else:
            return x
x = input()
print(round(x))
