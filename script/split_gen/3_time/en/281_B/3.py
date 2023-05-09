def check(s):
    if s[0].isupper() and s[7].isupper() and s[1:7].isdigit() and len(s[1:7])==6 and 100000<=int(s[1:7])<=999999:
        return "Yes"
    else:
        return "No"
s = input()
print(check(s))
