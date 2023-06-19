def check(s):
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdigit() and 100000 <= int(s[1:-1]) <= 999999:
        return "Yes"
    else:
        return "No"
s = input()
print(check(s))
