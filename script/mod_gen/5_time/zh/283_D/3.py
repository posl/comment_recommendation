def main():
    s = input()
    n = len(s)
    if n % 2 == 1:
        print('否')
        return
    cnt = 0
    for i in range(n):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1
        else:
            if cnt == 0:
                print('否')
                return
    print('是')

if __name__ == '__main__':
    main()