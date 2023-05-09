def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    if s == t:
        print('Yes')
        return
    s = sorted(s)
    t = sorted(t)
    if s == t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()