def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "v" and i+1 < len(s) and s[i+1] == "v":
            count += 1
    print(count * (count-1) // 2)

if __name__ == '__main__':
    main()