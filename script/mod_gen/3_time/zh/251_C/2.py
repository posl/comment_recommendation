def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    for i in range(n):
        if s[i] == s[i+1]:
            if t[i] > t[i+1]:
                t[i+1] = t[i]
                s[i+1] = s[i]
            else:
                t[i] = t[i+1]
                s[i] = s[i+1]
    print(s.index(s[n-1])+1)

if __name__ == '__main__':
    main()