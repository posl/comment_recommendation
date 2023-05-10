def main():
    n = int(input())
    s = input()
    if s[:n//2]*2 == s:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()