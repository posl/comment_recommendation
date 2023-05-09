def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a = 1
        b = 1
        while 4*a*b+3*a+3*b <= s[i]:
            if 4*a*b+3*a+3*b == s[i]:
                ans += 1
                break
            else:
                if a == b:
                    b += 1
                else:
                    a += 1
    print(n-ans)

if __name__ == '__main__':
    main()