def main():
    s = input()
    k = int(input())
    # print(s)
    # print(k)
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
        else:
            break
    if k <= count:
        print(1)
    else:
        print(s[count-1])

if __name__ == '__main__':
    main()