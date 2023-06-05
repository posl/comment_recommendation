def getMod(s):
    mod = 0
    for i in range(len(s)):
        mod = (mod*10+int(s[i]))%2019
    return mod
