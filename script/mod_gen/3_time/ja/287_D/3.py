def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[-(len(t)-i):]
        if s1+s2 == t:
            print("Yes")
        else:
            print("No")
main()

if __name__ == '__main__':
    main()