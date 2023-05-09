def main():
    x,y = map(int,input().split())
    if (x+y) == 1:
        print(2)
    elif (x+y) == 2:
        print(0)
    else:
        print(1)
