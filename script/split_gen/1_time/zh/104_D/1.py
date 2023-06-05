def main():
    s = input()
    l = len(s)
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(l):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
    ans = (a * b * c) % 1000000007
    for i in range(l):
        if s[i] == '?':
            a -= 1
            ans = (ans + a * b * c) % 1000000007
        elif s[i] == 'A':
            a -= 1
        elif s[i] == 'B':
            b -= 1
        elif s[i] == 'C':
            c -= 1
    print(ans)
