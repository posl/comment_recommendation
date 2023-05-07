def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if count == 0:
            count += 1
            print(count)
            continue
        if a[i] == a[i-1]:
            count += 1
            print(count)
        else:
            count = 1
            print(count)

if __name__ == '__main__':
    main()