def main():
    # Read a string:
    s = input()
    # Print a string:
    #print(s)
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Weak")
    elif s[0] == '9' and s[1] == '0' and s[2] == '1' and s[3] == '2':
        print("Weak")
    elif int(s[0]) + 1 == int(s[1]) and int(s[1]) + 1 == int(s[2]) and int(s[2]) + 1 == int(s[3]):
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()