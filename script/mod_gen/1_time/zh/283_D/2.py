def main():
    s = input()
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == '(':
            a += 1
        elif s[i] == ')':
            a -= 1
        else:
            b += 1
            if a > b:
                print('否')
                return
    if a == b:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()