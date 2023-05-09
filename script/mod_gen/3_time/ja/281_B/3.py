def main():
    s = input()
    if len(s) < 3:
        print("No")
        return
    if s[0].isupper() and s[-1].isupper():
        for i in range(1, len(s) - 1):
            if s[i].isdigit():
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    print("No")
    return

if __name__ == '__main__':
    main()