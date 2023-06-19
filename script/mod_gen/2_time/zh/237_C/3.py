def main():
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()