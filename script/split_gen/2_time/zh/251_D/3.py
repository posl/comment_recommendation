def main():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 2)
    elif w == 3:
        print(2)
        print(1, 2)
    elif w == 4:
        print(3)
        print(1, 2, 4)
    elif w == 5:
        print(3)
        print(1, 2, 4)
    elif w == 6:
        print(3)
        print(1, 2, 3)
    else:
        print(6)
        print(1, 2, 3, 4, 5, 6)
