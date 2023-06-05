def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            print(chr(64 + ord(s[i]) + n - 90), end='')
        else:
            print(chr(ord(s[i]) + n), end='')
    print()
