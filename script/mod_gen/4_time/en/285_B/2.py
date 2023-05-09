def main():
    n = int(input())
    s = input()
    for i in range(n-1):
        count = 0
        for j in range(n-i-1):
            if s[j] != s[j+i+1]:
                count += 1
            else:
                break
        print(count)

if __name__ == '__main__':
    main()