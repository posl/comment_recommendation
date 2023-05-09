def main():
    s = list(input())
    count = 0
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()