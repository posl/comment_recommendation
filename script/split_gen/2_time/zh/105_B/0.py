def main():
    n = int(input())
    if n%4 == 0 or n%7 == 0 or n%11 == 0:
        print('Yes')
    elif n%4 == 3:
        print('Yes')
    elif n%7 == 6:
        print('Yes')
    elif n%11 == 10:
        print('Yes')
    else:
        print('No')
