def main():
    n = int(input())
    s = input()
    if s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()