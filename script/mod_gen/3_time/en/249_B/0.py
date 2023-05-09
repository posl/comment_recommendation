def main():
    s = input()
    if s.isupper():
        print("No")
    elif s.islower():
        print("No")
    elif len(set(s)) != len(s):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()