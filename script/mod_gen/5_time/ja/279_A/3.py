def main():
    s = input()
    num = 0
    for i in range(len(s)):
        if s[i] == "w" and i != 0:
            if s[i-1] == "v":
                num += 1
    print(num)

if __name__ == '__main__':
    main()