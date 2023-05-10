def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(1, n):
        count += i - a[i-1]
        if a[i] == a[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()