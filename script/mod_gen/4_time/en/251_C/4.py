def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    #print(s)
    #print(t)
    maxt = max(t)
    #print(maxt)
    for i in range(n):
        if t[i] == maxt:
            print(s[i])
            break

if __name__ == '__main__':
    main()