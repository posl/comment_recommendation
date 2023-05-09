def main():
    A, B = map(int, input().split())
    if A + B > 16:
        print(':(')
    elif A > 8 or B > 8:
        print(':(')
    else:
        print('Yay!')

if __name__ == '__main__':
    main()