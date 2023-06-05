def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(len(a)):
        if a[i] > count:
            count += 1
    print(count)

if __name__ == '__main__':
    main()