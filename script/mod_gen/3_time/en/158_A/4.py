def main():
    S = input()
    if S.count('A') == 1 or S.count('B') == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()