def main():
    A, B = map(int, input().split())
    if 0 < A and B == 0:
        print('Gold')
    elif A == 0 and 0 < B:
        print('Silver')
    else:
        print('Alloy')
main()

if __name__ == '__main__':
    main()