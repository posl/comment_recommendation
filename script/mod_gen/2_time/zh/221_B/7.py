def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                s[i],s[i+1] = s[i+1],s[i]
                if s == t:
                    print("Yes")
                    break
                else:
                    print("No")
                    break
            else:
                print("No")
                break
        else:
            print("No")

if __name__ == '__main__':
    main()