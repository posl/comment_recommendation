def main():
    n = int(input())
    s = input()
    result = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            result += chr(ord(s[i]) + n - 26)
        else:
            result += chr(ord(s[i]) + n)
    print(result)
