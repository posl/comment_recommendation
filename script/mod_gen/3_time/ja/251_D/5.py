def main():
    w = int(input())
    if w <= 2:
        print('NO')
    elif w % 2 == 1:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()