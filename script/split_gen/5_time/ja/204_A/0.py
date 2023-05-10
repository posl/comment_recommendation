def janken(x,y):
    if x == y:
        return x
    else:
        return 3 - (x + y)
x,y = map(int,input().split())
print(janken(x,y))
