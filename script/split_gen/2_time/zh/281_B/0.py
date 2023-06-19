def main():
    s = input()
    if s[0].isupper() and s[-1].isupper():
        if len(s) == 8:
            if s[1:7].isdigit():
                if 100000 <= int(s[1:7]) <= 999999:
                    print("Yes")
                    exit()
    print("No")
