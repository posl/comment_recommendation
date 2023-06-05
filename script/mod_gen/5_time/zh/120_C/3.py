def main():
    s = input()
    red, blue = 0, 0
    for i in range(len(s)):
        if s[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

if __name__ == '__main__':
    main()