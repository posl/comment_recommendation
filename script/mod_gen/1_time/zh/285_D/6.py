def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == t[j]:
                    s[i], s[j] = s[j], s[i]
    if s == t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()