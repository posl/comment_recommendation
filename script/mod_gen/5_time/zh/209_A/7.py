def count_integers(a,b):
    # a,b = input("please input two numbers:").split()
    # a = int(a)
    # b = int(b)
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return b-a+1

if __name__ == '__main__':
    count_integers()