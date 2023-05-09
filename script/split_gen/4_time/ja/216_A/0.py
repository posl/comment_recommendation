def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print("{0}-".format(x))
    elif 3 <= y <= 6:
        print("{0}".format(x))
    else:
        print("{0}+".format(x))
