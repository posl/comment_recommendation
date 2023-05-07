def main():
    s = input()
    q = int(input())
    t = []
    f = []
    c = []
    for i in range(q):
        t.append(int(input()))
        if t[i] == 2:
            f.append(int(input()))
            c.append(input())
    ans = s
    for i in range(q):
        if t[i] == 1:
            ans = ans[::-1]
        else:
            if f[i] == 1:
                ans = c[i] + ans
            else:
                ans = ans + c[i]
    print(ans)

if __name__ == '__main__':
    main()