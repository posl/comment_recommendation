def main():
    s = input()
    q = s.count('?')
    p = 1
    for i in range(1,q+1):
        p = (p*3)%1000000007
    ans = 0
    c = 0
    for i in s:
        if i == 'C':
            c += 1
        elif i == 'B':
            ans += c*p
        elif i == '?':
            ans += c*p
            c = (c*2)%1000000007
    print(ans%1000000007)

if __name__ == '__main__':
    main()