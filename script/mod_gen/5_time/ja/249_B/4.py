def main():
    s = input()
    s1 = sorted(s)
    s2 = sorted(set(s))
    if s1 == s2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()