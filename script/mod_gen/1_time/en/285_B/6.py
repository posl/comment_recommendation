def main():
    n = int(input())
    s = input()
    for i in range(n):
        cnt = 0
        for j in range(n - i - 1):
            if s[j] != s[j + i + 1]:
                cnt += 1
            else:
                cnt = 0
            if j == n - i - 2:
                print(cnt)
main()

if __name__ == '__main__':
    main()