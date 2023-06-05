def main():
    s = input()
    if s.islower() or s.isupper() or len(s) < 2:
        print("No")
        return
    if len(s) % 2 != 0:
        print("No")
        return
    if s[0].islower():
        print("No")
        return
    if s[-1].isupper():
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()