def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 2:
        print('Yes')
    elif s.count('B') == 1 and s.count('A') == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()