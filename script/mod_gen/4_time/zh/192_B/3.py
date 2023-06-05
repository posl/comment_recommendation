def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 1:
            if s[i].isupper():
                print("No")
                return
        else:
            if s[i].islower():
                print("No")
                return
    print("Yes")
main()
