def main():
    n = int(input())
    s = []
    for _ in range(n):
        a,b = map(int, input().split())
        s.append((a,b))
    t = []
    for _ in range(n):
        a,b = map(int, input().split())
        t.append((a,b))
    if s == t:
        print('Yes')
        return
    for i in range(n):
        s = [(s[i][0]-s[0][0], s[i][1]-s[0][1]) for i in range(n)]
        t = [(t[i][0]-t[0][0], t[i][1]-t[0][1]) for i in range(n)]
        if s == t:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()