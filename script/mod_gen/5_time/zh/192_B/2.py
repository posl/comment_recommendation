def main():
    str = input()
    if len(str) == 1:
        print("Yes")
        return
    for i in range(0, len(str), 2):
        if str[i].isupper():
            print("No")
            return
    for i in range(1, len(str), 2):
        if str[i].islower():
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()