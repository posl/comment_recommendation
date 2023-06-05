def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    s = sorted(s)
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print("Yes")
    else:
        print("No")
