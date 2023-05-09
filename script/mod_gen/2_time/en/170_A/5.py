def main():
    #input
    x_1, x_2, x_3, x_4, x_5 = map(int, input().split())
    #output
    if x_1 == 0:
        print(1)
    elif x_2 == 0:
        print(2)
    elif x_3 == 0:
        print(3)
    elif x_4 == 0:
        print(4)
    else:
        print(5)

if __name__ == '__main__':
    main()