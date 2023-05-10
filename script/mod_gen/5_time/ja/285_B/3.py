def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                l += 1
            else:
                break
        count = max(count, l)
        print(count)

if __name__ == '__main__':
    main()