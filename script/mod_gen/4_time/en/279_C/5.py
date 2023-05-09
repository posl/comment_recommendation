def main():
    h, w = map(int, input().split())
    s = []
    t = []
    for i in range(h):
        s.append(input())
    for i in range(h):
        t.append(input())
    s = sorted(s)
    t = sorted(t)
    for i in range(h):
        if s[i] != t[i]:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()