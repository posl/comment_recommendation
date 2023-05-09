def main():
    A, B = map(int, input().split())
    if A == 1 and B == 1:
        print('No')
    elif A == 1 and B != 1:
        print('Yes')
    elif A != 1 and B == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()