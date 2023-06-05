def main():
    s = input()
    n = len(s)
    if n < 4:
        print(0)
        return
    count = 0
    for i in range(n-3):
        for j in range(i+3, n):
            if int(s[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()