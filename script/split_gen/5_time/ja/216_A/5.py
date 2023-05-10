def main():
    l = input().split(".")
    x = int(l[0])
    y = int(l[1])
    if 0 <= y <= 2:
        print(str(x) + "-")
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x) + "+")
