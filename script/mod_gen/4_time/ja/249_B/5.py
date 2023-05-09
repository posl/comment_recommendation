def main():
    s = input()
    s = sorted(s)
    s = "".join(s)
    if s.islower():
        print("No")
    elif s.isupper():
        print("No")
    elif len(s) == len(set(s)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()