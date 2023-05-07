def main():
    # A, B = map(int, input().split())
    A, B = 11, 4
    if A + B > 16:
        print(':(')
    elif A % 2 == 0 or B % 2 == 0:
        print(':(')
    else:
        print('Yay!')

if __name__ == '__main__':
    main()