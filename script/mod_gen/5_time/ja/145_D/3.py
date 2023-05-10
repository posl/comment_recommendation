def calc(x,y):
    if x < y:
        x,y = y,x
    if x == 1 and y == 1:
        return 0
    if x == 2 and y == 2:
        return 0
    if x == 1 and y == 2:
        return 1
    if x == 2 and y == 1:
        return 1
    if y == 0:
        return 1
    if y == 1:
        return 0
    if y == 2:
        return 0
    if x % 2 == 0:
        return calc(x//2,y-1)
    else:
        return calc(x//2,y-1) + calc(x//2+1,y-1)
x,y = map(int,input().split())
print(calc(x,y) % (10**9+7))

if __name__ == '__main__':
    calc()