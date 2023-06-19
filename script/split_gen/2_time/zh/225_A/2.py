def main():
    s = input()
    print(3 if s[0] == s[1] == s[2] else 1 if s[0] == s[1] or s[1] == s[2] else 6)
