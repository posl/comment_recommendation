def main():
    s = input()
    t = s[::-1]
    if s == t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()