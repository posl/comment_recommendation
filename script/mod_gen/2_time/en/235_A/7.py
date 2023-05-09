def main():
    a, b, c = map(int, input())
    print(a+b+c, b+c+a, c+a+b, sep='')

if __name__ == '__main__':
    main()