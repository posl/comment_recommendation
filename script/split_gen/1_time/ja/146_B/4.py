def main():
    n = int(input())
    s = input()
    ans = ''
    for i in range(len(s)):
        if ord(s[i]) + n > ord('Z'):
            ans += chr(ord(s[i]) + n - ord('Z') + ord('A') - 1)
        else:
            ans += chr(ord(s[i]) + n)
    print(ans)
