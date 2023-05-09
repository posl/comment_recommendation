def main():
    s = input()
    q = s.count("?")
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    ans = 0
    for i in range(len(s)):
        if s[i] == "A":
            a -= 1
        elif s[i] == "B":
            b -= 1
        elif s[i] == "C":
            c -= 1
        elif s[i] == "?":
            q -= 1
            ans += (a*pow(3,q,10**9+7)+b*pow(3,q,10**9+7)+c*pow(3,q,10**9+7))
            ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()