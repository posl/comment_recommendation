def main():
    s = input()
    if s[0].isupper() and s[-1].isupper():
        if s[1:-1].isdecimal() and len(s[1:-1]) == 6:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
