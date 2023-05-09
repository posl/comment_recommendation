def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s = s[:i] + chr(ord(s[i]) + n - 26) + s[i+1:]
        else:
            s = s[:i] + chr(ord(s[i]) + n) + s[i+1:]
    print(s)
