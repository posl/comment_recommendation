def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(1, l):
        ans += 26**i
    ans += (ord(s[0])-ord('A')) * 26**(l-1)
    print(ans+1)
