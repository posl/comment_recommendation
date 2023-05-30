def shift(s, n):
    return ''.join(chr((ord(c) - ord('A') + n) % 26 + ord('A')) for c in s)
n = int(input())
s = input()
print(shift(s, n))
