def main():
    s = input()
    #print(s)
    if len(s) != 9:
        print("No")
        return
    if s[0].isupper() and s[8].isupper():
        if s[1:7].isdigit():
            if 100000 <= int(s[1:7]) <= 999999:
                print("Yes")
                return
    print("No")
main()
