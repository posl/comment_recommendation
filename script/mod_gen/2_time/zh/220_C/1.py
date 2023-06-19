def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum = 0
    for i in range(10 ** 100):
        sum += a[i % n]
        if sum > x:
            print(i + 1)
            break

if __name__ == '__main__':
    main()