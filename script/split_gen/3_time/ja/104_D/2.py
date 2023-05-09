def main():
    s = input()
    n = len(s)
    a = []
    b = []
    c = []
    q = 0
    for i in range(n):
        if s[i] == 'A':
            a.append(i)
        elif s[i] == 'B':
            b.append(i)
        elif s[i] == 'C':
            c.append(i)
        else:
            q += 1
    ans = 0
    for i in range(len(b)):
        ans += len(a) * (len(c) + len(b) + len(c) - b[i])
    print(ans % (10**9+7))
