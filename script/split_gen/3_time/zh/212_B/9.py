def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Weak")
        return
    if (int(s[0]) + 1) % 10 == int(s[1]) and (int(s[1]) + 1) % 10 == int(s[2]) and (int(s[2]) + 1) % 10 == int(s[3]):
        print("Weak")
        return
    print("Strong")
