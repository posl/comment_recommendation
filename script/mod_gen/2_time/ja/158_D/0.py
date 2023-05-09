def main():
    s = input()
    q = int(input())
    t = [0] * q
    f = [0] * q
    c = [0] * q
    for i in range(q):
        t[i], f[i], c[i] = input().split()
        t[i] = int(t[i])
        f[i] = int(f[i])
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