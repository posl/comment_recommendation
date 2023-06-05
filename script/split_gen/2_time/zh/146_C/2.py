def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s[i] = chr(ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n)
    print(''.join(s))
