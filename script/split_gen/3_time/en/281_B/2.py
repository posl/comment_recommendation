def main():
    s = input()
    if len(s) != 10:
        print("No")
        return
    if s[0].isupper() and s[9].isupper():
        if s[1:7].isdecimal():
            if 100000 <= int(s[1:7]) <= 999999:
                print("Yes")
                return
    print("No")
