def main():
    x, y = map(int, input().split("."))
    if y < 3:
        print(x, "-", sep="")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x, "+", sep="")
