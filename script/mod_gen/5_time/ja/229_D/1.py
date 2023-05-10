def main():
    s = input()
    k = int(input())
    count = 0
    for i in range(len(s)):
        if i == 0:
            if s[i] == "X":
                count += 1
        elif s[i] == "X":
            if s[i-1] == "X":
                count += 1
            else:
                count = 1
        else:
            count = 0
        if count >= k:
            count = k
            break
    print(count)

if __name__ == '__main__':
    main()