def check(s):
    for i in range(3):
        if s[i] == s[i+1]:
            return "Bad"
    return "Good"
s = input()
print(check(s))
