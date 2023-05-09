def main():
    s = input()
    s_rev = s[::-1]
    for i in range(len(s)):
        if s[i] == s_rev[i]:
            continue
        else:
            s = s + 'a'
            s_rev = s[::-1]
    print('Yes')
