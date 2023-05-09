def main():
    a, b, c = [int(x) for x in input().split()]
    if b > a and b < c or b < a and b > c:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()