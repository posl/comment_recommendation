def main():
    s = input()
    q = s.count("?")
    mod = 10**9 + 7
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == "A":
            a += 1
        elif s[i] == "B":
            b += 1
        elif s[i] == "C":
            c += 1
    for i in range(len(s)):
        if s[i] == "B" or s[i] == "?":
            ans += a * c * pow(3, q, mod)
            if s[i] == "?":
                q -= 1
        if s[i] == "A":
            a -= 1
        if s[i] == "C":
            c -= 1
    print(ans % mod)
