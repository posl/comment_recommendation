def main():
    s = input()
    s1 = s.lower()
    if s1 != s and s1.lower() == s:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()