def main():
    s = input()
    if s.islower():
        print("No")
        return
    if s.isupper():
        print("No")
        return
    if s[0].islower():
        print("No")
        return
    if s[-1].isupper():
        print("No")
        return
    print("Yes")
main()
