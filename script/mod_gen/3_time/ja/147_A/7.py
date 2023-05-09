def main():
    #input_line = input()
    #a, b, c = input_line.split()
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b + c >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()