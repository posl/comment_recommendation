def main():
    s = input()
    i = 0
    n = 0
    while i < len(s):
        if i == 0:
            n += (ord(s[i])-64)
        else:
            n += (ord(s[i])-64) * (26**i)
        i += 1
    print(n)
