def main():
    a = int(input())
    b = int(input())
    if a == b:
        print(str(a) * a)
    elif a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

if __name__ == '__main__':
    main()