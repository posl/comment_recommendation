def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == 'a':
            continue
        if s[i] <= 'c':
            ans += 2
        elif s[i] <= 'e':
            ans += 3
        elif s[i] <= 'r':
            ans += 4
        elif s[i] <= 't':
            ans += 5
        elif s[i] <= 'd':
            ans += 6
        elif s[i] <= 'o':
            ans += 7
        else:
            ans += 8
    print(ans)
