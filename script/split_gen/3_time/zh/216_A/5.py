def main():
    x, y = map(float, input().split("."))
    if y <= 2:
        print(str(int(x)) + "-")
    elif y <= 6:
        print(int(x))
    else:
        print(str(int(x)) + "+")
