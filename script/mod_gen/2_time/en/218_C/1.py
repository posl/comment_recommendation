def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    if s == t:
        print('Yes')
        return
    for i in range(1, 4):
        s = list(map(list, zip(*s[::-1])))
        if s == t:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()