def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)-1):
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()