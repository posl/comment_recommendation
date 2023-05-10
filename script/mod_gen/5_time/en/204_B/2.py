def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] > 10:
            count += a[i] - 10
    print(count)

if __name__ == '__main__':
    main()