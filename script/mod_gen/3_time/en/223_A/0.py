def main():
    X = int(input())
    if X == 0:
        print('No')
    elif X % 100 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()