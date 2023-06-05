def main():
    n = int(input())
    s = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        a = 1
        b = 1
        while 4*a*b+3*a+3*b <= s[i]:
            if 4*a*b+3*a+3*b == s[i]:
                cnt += 1
            b += 1
        a += 1
    print(n-cnt)

if __name__ == '__main__':
    main()