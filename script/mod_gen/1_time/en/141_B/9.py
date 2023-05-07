def main():
    s = input()
    if len(s) == 1:
        print("Yes")
        return
    if len(s) % 2 == 0:
        print("Yes" if s[::2].count("L") == 0 and s[1::2].count("R") == 0 else "No")
    else:
        print("No")

if __name__ == '__main__':
    main()