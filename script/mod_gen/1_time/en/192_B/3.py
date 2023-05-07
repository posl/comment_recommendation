def main():
    s = input()
    if s[::2].islower() and s[1::2].isupper():
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()