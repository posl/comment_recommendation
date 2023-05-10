def main():
    S = input()
    if S.count('o') + 15 - len(S) >= 8:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()