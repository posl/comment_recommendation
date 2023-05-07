def main():
    s = input()
    if s[0::2].islower() and s[1::2].isupper():
        print("Yes")
    else:
        print("No")
main()
