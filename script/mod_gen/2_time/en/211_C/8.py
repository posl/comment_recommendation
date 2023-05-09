def  main():
    s = input()
    MOD = 10**9 + 7
    a = [0]*8
    for i in range(len(s)):
        if s[i] == 'c':
            a[0] += 1
        elif s[i] == 'h':
            a[1] += a[0]
        elif s[i] == 'o':
            a[2] += a[1]
        elif s[i] == 'k':
            a[3] += a[2]
        elif s[i] == 'u':
            a[4] += a[3]
        elif s[i] == 'd':
            a[5] += a[4]
        elif s[i] == 'a':
            a[6] += a[5]
        elif s[i] == 'i':
            a[7] += a[6]
    print(a[7]%MOD)

if __name__ == '__main__':
    ()