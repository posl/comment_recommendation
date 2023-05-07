def main():
    s = input()
    ans = 0
    if s[0] == 'o':
        ans = 1
    elif s[0] == 'x':
        ans = 0
    else:
        ans = 10
    for i in range(1, len(s)):
        if s[i] == 'o':
            ans = ans * 9
        elif s[i] == 'x':
            ans = ans * 9
        else:
            ans = ans * 10
    print(ans)
