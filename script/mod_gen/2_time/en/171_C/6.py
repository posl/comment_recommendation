def getDogName(n):
    if n == 0:
        return ""
    else:
        return getDogName((n-1)/26) + chr(ord('a') + (n-1)%26)
n = int(raw_input())
print getDogName(n)
