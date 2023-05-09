def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input().split()[0])
        t.append(input().split()[1])
    for i in range(n):
        if s[i] in s[:i] or s[i] in s[i+1:] or s[i] in t[:i] or s[i] in t[i+1:]:
            if t[i] in s[:i] or t[i] in s[i+1:] or t[i] in t[:i] or t[i] in t[i+1:]:
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()