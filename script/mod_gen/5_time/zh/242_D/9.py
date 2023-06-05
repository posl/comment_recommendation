def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        if t == 0:
            print(s[k])
        elif t == 1:
            if s[k] == 'a':
                print('b')
            elif s[k] == 'b':
                print('c')
            elif s[k] == 'c':
                print('a')
        elif t == 2:
            if s[k] == 'a':
                print('c')
            elif s[k] == 'b':
                print('a')
            elif s[k] == 'c':
                print('b')

if __name__ == '__main__':
    main()