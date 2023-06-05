def check(s):
    for i in range(len(s)):
        if i%2 == 0:
            if s[i].islower():
                return False
        else:
            if s[i].isupper():
                return False
    return True
s = input()
print("Yes" if check(s) else "No")
