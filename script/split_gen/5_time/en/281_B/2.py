def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and len(s) == 8 and s[1:7].isdigit() and int(s[1:7]) >= 100000 and int(s[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")
