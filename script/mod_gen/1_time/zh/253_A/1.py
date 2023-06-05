def median(a,b,c):
    if ((a>b and a<c) or (a>c and a<b)):
        return True
    else:
        return False

if __name__ == '__main__':
    median()