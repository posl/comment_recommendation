def main():
    x,y = map(float,input().split("."))
    if 0 <= y <= 2:
        print(int(x) - 1,end="")
        print("-")
    elif 3 <= y <= 6:
        print(int(x))
    else:
        print(int(x) + 1,end="")
        print("+")
