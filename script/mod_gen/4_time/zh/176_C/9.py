def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if a[i] <= max:
            count += max - a[i]
        else:
            max = a[i]
    print(count)

if __name__ == '__main__':
    main()