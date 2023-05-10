def main():
    s = input()
    if s[0].isupper() and s[7].isupper() and s[1:7].isdigit() and 100000 <= int(s[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")
