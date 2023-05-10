def main():
    s = input()
    ans = 0
    a = 0
    b = 0
    c = 0
    q = 0
    for i in range(len(s)):
        if s[i] == "A":
            a += 1
        elif s[i] == "B":
            b += 1
        elif s[i] == "C":
            c += 1
        elif s[i] == "?":
            q += 1
    for i in range(len(s)):
        if s[i] == "A":
            a -= 1
        elif s[i] == "B":
            b -= 1
        elif s[i] == "C":
            c -= 1
        elif s[i] == "?":
            q -= 1
        if s[i] == "B" or s[i] == "?":
            ans += a * c * pow(3, q, mod)
    print(ans % mod)
