def main():
    a = int(input())
    b = int(input())
    c = 0
    if a == 1:
        if b == 2:
            c = 3
        else:
            c = 2
    elif a == 2:
        if b == 1:
            c = 3
        else:
            c = 1
    else:
        if b == 1:
            c = 2
        else:
            c = 1
    print(c)
