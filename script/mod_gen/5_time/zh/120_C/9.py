def main():
    s = input()
    n = len(s)
    if n == 1:
        print(0)
        return
    count = 0
    for i in range(n):
        if s[i] == '0':
            count += 1
    print(min(count, n-count)*2)

if __name__ == '__main__':
    main()