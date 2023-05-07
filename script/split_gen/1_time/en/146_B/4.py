def main():
    n = int(input())
    s = input()
    for c in s:
        if c == ' ':
            print(' ', end='')
        else:
            print(chr(ord('A') + (ord(c) - ord('A') + n) % 26), end='')
    print()
