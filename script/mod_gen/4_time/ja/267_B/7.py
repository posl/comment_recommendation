def main():
    s = input()
    if s[0] == "0":
        print("No")
        return
    if s[4] == "0" or s[5] == "0":
        print("No")
        return
    if s[6] == "0" or s[7] == "0":
        print("No")
        return
    if s[8] == "0" or s[9] == "0":
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()