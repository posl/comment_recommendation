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
            if i != j and s[i] == t[j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()