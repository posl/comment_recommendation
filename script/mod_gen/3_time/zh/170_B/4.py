def func(x,y):
    if 2*x <= y and y <= 4*x:
        return "Yes"
    else:
        return "No"
x,y = map(int,input().split())
print(func(x,y))
