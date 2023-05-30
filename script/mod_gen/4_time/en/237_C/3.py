def main():
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            if s[:i] == s[i+1:][::-1]:
                print("Yes")
            elif s[:n-i-1] == s[n-i:][::-1]:
                print("Yes")
            else:
                print("No")
            exit()
    print("Yes")
main()
