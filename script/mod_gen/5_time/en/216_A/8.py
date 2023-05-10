def main():
    input = raw_input()
    input = input.split('.')
    x = int(input[0])
    y = int(input[1])
    if y <= 2:
        print str(x) + "-"
    elif y <= 6:
        print str(x)
    else:
        print str(x) + "+"

if __name__ == '__main__':
    main()