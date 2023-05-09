def main():
    s = input()
    if s.islower() == True or s.isupper() == True:
        print("No")
    else:
        if len(s) == len(set(s)):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()