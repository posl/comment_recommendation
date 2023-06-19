def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        x, y = input().split()
        s.append(x)
        t.append(y)
    for i in range(n):
        for j in range(n):
            if s[i] == t[j]:
                if t[i] == s[j]:
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()