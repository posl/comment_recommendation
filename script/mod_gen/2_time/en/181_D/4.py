def main():
    s = input()
    if s == '8':
        print('Yes')
        return
    if len(s) == 1:
        print('No')
        return
    if len(s) == 2:
        if int(s) % 8 == 0:
            print('Yes')
            return
        if int(s[::-1]) % 8 == 0:
            print('Yes')
            return
        print('No')
        return
    s = sorted(s)
    for i in range(104, 1000, 8):
        if sorted(str(i)) == s:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()