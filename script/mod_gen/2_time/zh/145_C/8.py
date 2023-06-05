def main():
    n = int(input())
    s = input()
    print("Yes" if s[0:n//2] == s[n//2:] else "No")

if __name__ == '__main__':
    main()