def main():
    s = input()
    if s[0].isupper() and s[1:7].isdigit() and s[7].isupper():
        print("Yes")
    else:
        print("No")
