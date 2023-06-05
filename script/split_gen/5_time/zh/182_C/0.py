def main():
    N = int(input())
    if N % 3 == 0:
        print(0)
    elif N % 3 == 1:
        if N % 10 == 1:
            print(1)
        elif N % 10 == 4:
            print(1)
        elif N % 10 == 7:
            print(1)
        else:
            print(2)
    else:
        if N % 10 == 2:
            print(1)
        elif N % 10 == 5:
            print(1)
        elif N % 10 == 8:
            print(1)
        else:
            print(2)
