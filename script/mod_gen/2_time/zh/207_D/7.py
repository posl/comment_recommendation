def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    for i in range(n):
        t.append(list(map(int, input().split())))
    s.sort()
    t.sort()
    for i in range(n):
        for j in range(n):
            if s[i][0] == t[j][0] and s[i][1] == t[j][1]:
                s[i][0] = 'x'
                s[i][1] = 'x'
                t[j][0] = 'x'
                t[j][1] = 'x'
    for i in range(n):
        if s[i][0] != 'x' or s[i][1] != 'x':
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()