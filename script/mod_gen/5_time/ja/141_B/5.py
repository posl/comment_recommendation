def main():
    s = input()
    s1 = s[0::2]
    s2 = s[1::2]
    if s1.count("R") == len(s1) and s2.count("L") == len(s2):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()