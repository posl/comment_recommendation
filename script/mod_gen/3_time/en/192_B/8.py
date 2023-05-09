def main():
    s = input()
    if len(s) == 1:
        print("Yes")
    else:
        for i in range(0, len(s), 2):
            if s[i].islower() == False:
                print("No")
                return
        for i in range(1, len(s), 2):
            if s[i].isupper() == False:
                print("No")
                return
        print("Yes")

if __name__ == '__main__':
    main()