def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = map(str, input().split())
        s.append(a)
        t.append(b)
    # print(s)
    # print(t)
    for i in range(n):
        if s[i] == t[i]:
            print('No')
            exit()
        for j in range(i+1, n):
            if s[i] == t[j] and s[j] == t[i]:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()