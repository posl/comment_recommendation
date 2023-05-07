def main():
    a = input()
    b = list(map(int, a.split()))
    c = sorted(b)
    if c[0] == c[1] and c[1] == c[2] and c[3] == c[4]:
        print('Yes')
    elif c[0] == c[1] and c[2] == c[3] and c[3] == c[4]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()