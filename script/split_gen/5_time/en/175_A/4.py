def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(3)
    elif s[0] == s[1] != s[2] or s[0] != s[1] == s[2]:
        print(2)
    else:
        print(1)
