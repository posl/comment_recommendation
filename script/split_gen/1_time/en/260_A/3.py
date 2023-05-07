def main():
    s = input()
    if len(s) == 3:
        if s[0] == s[1]:
            if s[0] == s[2]:
                print("-1")
            else:
                print(s[2])
        else:
            if s[0] == s[2]:
                print(s[1])
            else:
                print(s[0])
    else:
        print("-1")
