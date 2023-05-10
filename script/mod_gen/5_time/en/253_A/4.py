def main():
    a,b,c = map(int, input().split())
    if b > a and b < c or b < a and b > c:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()