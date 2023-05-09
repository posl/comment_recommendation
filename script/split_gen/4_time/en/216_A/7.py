def main():
    import sys
    input = sys.stdin.readline
    x,y = input().rstrip().split(".")
    y = int(y)
    if y <= 2:
        print(x+"-")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x+"+")
