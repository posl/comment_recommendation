def main():
    n = int(input())
    t = []
    a = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        t.append(tmp[0])
        a.append(tmp[2:])
    s = [0] * n
    for i in range(n):
        s[i] = t[i]
        if a[i]:
            for j in a[i]:
                s[i] = max(s[i],s[j-1] + t[i])
    print(max(s))

if __name__ == '__main__':
    main()