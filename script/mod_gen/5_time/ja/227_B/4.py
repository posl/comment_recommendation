def main():
    n = int(input())
    s = list(map(int, input().split()))
    c = 0
    for i in range(n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if (a + 3) * (b + 3) == s[i] + 3:
                    c += 1
                    break
            a += 1
    print(n - c)

if __name__ == '__main__':
    main()