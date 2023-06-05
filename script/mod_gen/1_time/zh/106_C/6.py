def main():
    s = input()
    k = int(input())
    if s[0] != '1':
        print(s[0])
    else:
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                break
        if count >= k:
            print('1')
        else:
            print(s[count])

if __name__ == '__main__':
    main()