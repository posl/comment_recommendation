def func():
    x,y = input().split(".")
    y = int(y)
    if y <= 2:
        print(int(x)+"-")
    elif y >= 7:
        print(int(x)+"+")
    else:
        print(int(x))
func()
