def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
        print("No")
    else:
        print("Yes")