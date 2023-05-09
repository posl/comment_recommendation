def main():
    str = input()
    red = 0
    blue = 0
    for i in str:
        if i == '0':
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

if __name__ == '__main__':
    main()