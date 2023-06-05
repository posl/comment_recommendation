def main():
    s = input()
    count = 0
    for i in range(len(s)):
        for j in range(i+3,len(s)):
            if int(s[i:j+1])%2019 == 0:
                count +=1
    print(count)

if __name__ == '__main__':
    main()