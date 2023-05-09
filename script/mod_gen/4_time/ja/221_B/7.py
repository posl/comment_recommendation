def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(len(s)-1):
        if s[i+1] + s[i] == t[i+1] + t[i]:
            print("Yes")
            exit()
    print("No")
main()

if __name__ == '__main__':
    main()