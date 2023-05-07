def main():
    a, b = map(int, input().split())
    if a >= b:
        print('Yes')
    elif a == 1:
        print('No')
    elif a == 2:
        if b % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')
