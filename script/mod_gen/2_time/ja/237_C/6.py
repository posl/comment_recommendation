def main():
    s = input()
    s = s + s[::-1]
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()