def main():
    x,y=input().split(".")
    y=int(y)
    x=int(x)
    if 0<=y<=2:
        print(x,end="")
        print("-")
    elif 3<=y<=6:
        print(x,end="")
    elif 7<=y<=9:
        print(x,end="")
        print("+")
