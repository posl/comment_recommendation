def main():
    n = input()
    n = int(n)
    if n%3 == 0:
        print(0)
    elif n%3 == 1:
        if n%10 == 1:
            print(-1)
        elif n%10 == 4:
            print(1)
        else:
            print(2)
    else:
        if n%10 == 2:
            print(-1)
        elif n%10 == 5:
            print(1)
        else:
            print(2)
