def main():
    # input
    a, b = map(int, input().split())
    # compute
    if a+b >= 100:
        print(4)
    elif a+b >= 80:
        print(3)
    elif a+b >= 60:
        print(2)
    else:
        print(1)
    # output

if __name__ == '__main__':
    main()