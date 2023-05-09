def main():
    n = int(input())
    s = input()
    s = list(s)
    count = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()