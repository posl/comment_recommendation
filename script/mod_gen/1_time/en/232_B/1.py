def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(1, len(s)):
            if s[i:] + s[:i] == t:
                print("Yes")
                break
        else:
            print("No")
main()
