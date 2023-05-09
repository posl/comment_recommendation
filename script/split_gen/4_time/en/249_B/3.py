def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    else:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                print("No")
                break
        else:
            print("Yes")
main()
