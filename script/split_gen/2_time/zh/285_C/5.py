def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans = ans * 26 + ord(s[i]) - ord('A') + 1
    print(ans)
