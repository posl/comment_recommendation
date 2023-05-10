def main():
    s = input()
    k = int(input())
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    print(min(count+2*k,len(s)-1))

if __name__ == '__main__':
    main()