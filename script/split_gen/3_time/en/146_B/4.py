def shift(s, n):
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s = s[:i] + chr(ord(s[i]) + n - 26) + s[i+1:]
        else:
            s = s[:i] + chr(ord(s[i]) + n) + s[i+1:]
    return s
n = int(input())
s = input()
print(shift(s, n))
