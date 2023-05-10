def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(b)
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                if t[i] == t[j]:
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()