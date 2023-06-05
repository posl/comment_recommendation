def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    num = 7
    for i in range(1, k + 1):
        if num % k == 0:
            print(i)
            return
        num = num * 10 + 7
        num %= k
    print(-1)

if __name__ == '__main__':
    main()