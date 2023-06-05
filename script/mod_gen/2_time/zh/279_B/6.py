def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "w":
            count += 1
            for j in range(i+1,len(s)):
                if s[j] == "v":
                    count += 1
                else:
                    break
    print(count)

if __name__ == '__main__':
    main()