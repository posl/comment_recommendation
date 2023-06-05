def main():
    n = int(input())
    s = input()
    if len(s) % 2 == 0:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        if s1 == s2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()