def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if s[i] % 2 == 0:
            count += 1
        else:
            if s[i] % 3 == 0:
                count += 1
            else:
                if s[i] % 5 == 0:
                    count += 1
                else:
                    pass
    print(n - count)

if __name__ == '__main__':
    main()