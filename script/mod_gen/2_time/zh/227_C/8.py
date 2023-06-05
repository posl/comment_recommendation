def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if 4 * a * b + 3 * a + 3 * b == s[i]:
                    break
            a += 1
        if a * a > s[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()