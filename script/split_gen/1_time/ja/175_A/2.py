def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2]:
        print(2)
    else:
        print(0)
