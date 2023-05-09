def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        count = 0
        for j in range(n - i):
            if s[j] != s[j + i]:
                count += 1
        print(count)
    return

if __name__ == '__main__':
    main()