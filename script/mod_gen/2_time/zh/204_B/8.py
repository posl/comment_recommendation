def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if a[i] > 10:
            sum += a[i] - 10
    print(sum)

if __name__ == '__main__':
    main()