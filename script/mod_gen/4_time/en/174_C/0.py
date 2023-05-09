def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        n = 7 % k
        for i in range(1, k + 1):
            if n == 0:
                print(i)
                break
            n = (n * 10 + 7) % k

if __name__ == '__main__':
    main()