def main():
    s = input()
    if s[::2].count("L") == 0 and s[1::2].count("R") == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()