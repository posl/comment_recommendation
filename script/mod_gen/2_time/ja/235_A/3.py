def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c, b+c+a, c+a+b, sep='')

if __name__ == '__main__':
    main()