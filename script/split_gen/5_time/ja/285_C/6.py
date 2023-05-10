def main():
    import sys
    import math
    s = sys.stdin.readline().strip()
    n = len(s)
    if n == 1:
        print(ord(s[0]) - ord('A') + 1)
    elif n == 2:
        print((ord(s[0]) - ord('A') + 1) * 26 + ord(s[1]) - ord('A') + 1)
    elif n == 3:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 + ord(s[2]) - ord('A') + 1)
    elif n == 4:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 * 26 + (ord(s[2]) - ord('A') + 1) * 26 + ord(s[3]) - ord('A') + 1)
    elif n == 5:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 * 26 * 26 + (ord(s[2]) - ord('A') + 1) * 26 * 26 + (ord(s[3]) - ord('A') + 1) * 26 + ord(s[4]) - ord('A') + 1)
    elif n == 6:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 * 26 * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 * 26 * 26 * 26 + (ord(s[2]) - ord('A') + 1) * 26 * 26 * 26 + (ord(s[3]) - ord('A') + 1) * 26 * 26 + (ord(s[4]) - ord('A') + 1) * 26 + ord(s[5]) -
