def main():
    n = int(input())
    s = list(input())
    ans = []
    for i in range(len(s)):
        ans.append(chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')))
    print(''.join(ans))
