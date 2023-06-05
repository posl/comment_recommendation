def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    x = 7
    for i in range(1, k + 1):
        if x % k == 0:
            print(i)
            return
        x = x * 10 + 7
        x %= k
    print(-1)

if __name__ == '__main__':
    main()