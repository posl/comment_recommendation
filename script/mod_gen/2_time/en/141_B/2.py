def main():
    s = input()
    if s[::2].count("R") + s[1::2].count("L") == len(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()