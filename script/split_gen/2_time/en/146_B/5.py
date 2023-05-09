def shift_char(c, n):
    if ord(c) + n > ord('Z'):
        return chr(ord(c) + n - 26)
    else:
        return chr(ord(c) + n)
n = int(input())
s = input()
for c in s:
    print(shift_char(c, n), end="")
Related
