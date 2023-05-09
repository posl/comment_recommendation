def main():
    s = input()
    #print(s)
    #print(s[::-1])
    cnt = 0
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            cnt += 1
    print(cnt//2)

if __name__ == '__main__':
    main()