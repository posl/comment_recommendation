def check(x,y):
    if x*2 <= y and y <= x*4 and y%2 == 0:
        return True
    else:
        return False
x,y = map(int,input().split())
