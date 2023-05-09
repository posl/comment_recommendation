def intToName(n):
    if n == 0:
        return ""
    else:
        return intToName((n-1)/26) + chr((n-1)%26 + 97)
n = input()
print intToName(n)
