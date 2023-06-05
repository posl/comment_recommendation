def f(x,y):
    if x==0 and y==0:
        return '0'
    if x>0 and y==0:
        return 'R'
    if x<0 and y==0:
        return 'L'
    if x==0 and y>0:
        return 'U'
    if x==0 and y<0:
        return 'D'
    if x>0 and y>0:
        return 'RU'
    if x>0 and y<0:
        return 'RD'
    if x<0 and y>0:
        return 'LU'
    if x<0 and y<0:
        return 'LD'

if __name__ == '__main__':
    f()