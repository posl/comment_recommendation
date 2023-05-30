def shift(s, shift):
    return ''.join(chr(((ord(c) - ord('A') + shift) % 26) + ord('A')) for c in s)
n = int(input())
s = input()
print(shift(s, n))
