def main():
    s = input()
    t = input()
    if len(s) == len(t):
        if s == t:
            print("Yes")
        else:
            for i in range(len(s) - 1):
                if s[i] == t[i+1] and s[i+1] == t[i]:
                    print("Yes")
                    break
            else:
                print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()