def main():
    s = input()
    n = len(s)
    mod = 10**9+7
    ans = 0
    a = 0
    ab = 0
    abc = 0
    for i in range(n):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            ab += a
        elif s[i] == 'C':
            abc += ab
        else:
            abc = 3*abc + ab
            ab = 3*ab + a
            a = 3*a + 1
    ans = abc % mod
    print(ans)

if __name__ == '__main__':
    main()