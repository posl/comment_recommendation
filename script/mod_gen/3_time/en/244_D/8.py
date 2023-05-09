def main():
    s = list(input())
    t = list(input())
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()