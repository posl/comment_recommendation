def main():
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        print('Alloy')
    elif A == 0:
        print('Silver')
    elif B == 0:
        print('Gold')
    else:
        print('Alloy')

if __name__ == '__main__':
    main()