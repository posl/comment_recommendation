def main():
    # Write code here
    s = input()
    atcoder = 'atcoder'
    ans = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            ans += abs(ord(s[i]) - ord(atcoder[i]))
    print(ans)
