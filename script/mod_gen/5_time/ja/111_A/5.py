def main():
    n = int(input())
    print(str(n).replace('1', 'x').replace('9', '1').replace('x', '9'))

if __name__ == '__main__':
    main()