def main():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n / 200
        else:
            n = int(str(n) + '200')
    print(int(n))

if __name__ == '__main__':
    main()