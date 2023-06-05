def moveN(s, n):
    l = len(s)
    if n == 0:
        return s
    elif n > 0:
        n = n % 26
        s1 = ''
        for i in range(l):
            if ord(s[i]) + n > 90:
                s1 += chr(ord(s[i]) + n - 26)
            else:
                s1 += chr(ord(s[i]) + n)
        return s1
    else:
        n = n % 26
        s1 = ''
        for i in range(l):
            if ord(s[i]) + n < 65:
                s1 += chr(ord(s[i]) + n + 26)
            else:
                s1 += chr(ord(s[i]) + n)
        return s1
n = int(input())
s = input()
print(moveN(s, n))
