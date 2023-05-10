def main():
    s = input()
    n = len(s)
    mod = 10 ** 9 + 7
    a = 0
    b = 0
    c = 0
    ans = 0
    for i in range(n):
        if s[i] == "A":
            a += 1
        elif s[i] == "B":
            b += 1
        elif s[i] == "C":
            c += 1
        else:
            ans = (ans * 3 + c) % mod
            c = (c * 3 + b) % mod
            b = (b * 3 + a) % mod
            a = (a * 3 + 1) % mod
    print(ans)
