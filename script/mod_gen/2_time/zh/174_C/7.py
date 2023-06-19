def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    i = 1
    num = 7
    while num % k != 0:
        num = num * 10 + 7
        num %= k
        i += 1
    print(i)

if __name__ == '__main__':
    main()