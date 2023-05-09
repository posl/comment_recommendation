def median(a,b,c):
    if (a <= b <= c) or (c <= b <= a):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    median()