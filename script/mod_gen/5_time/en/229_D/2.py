def main():
    s = input()
    k = int(input())
    s = s.replace('X', 'X.')
    s = s.replace('..', '.')
    s = s.replace('X.', 'X')
    s = s.replace('..', '.')
    s = s.replace('X.', 'X')
    s = s.replace('..', '.')
    print(len(s) - 1)

if __name__ == '__main__':
    main()