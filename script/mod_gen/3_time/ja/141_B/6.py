def main():
    s = input()
    for i in range(0,len(s),2):
        if s[i] in "L":
            print("No")
            exit()
    for i in range(1,len(s),2):
        if s[i] in "R":
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()