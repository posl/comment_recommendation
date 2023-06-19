def mid(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False
a,b,c = map(int,input().split())

if __name__ == '__main__':
    mid()