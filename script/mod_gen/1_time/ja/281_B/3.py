def main():
    s = input()
    if s[0].isupper() and s[-1].isupper():
        for i in range(1,len(s)-1):
            if s[i].isupper():
                print("No")
                return
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()