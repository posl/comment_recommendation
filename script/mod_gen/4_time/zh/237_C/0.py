def main():
    s = input()
    # print(s)
    # print(s[::-1])
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()