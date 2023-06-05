def main():
    n = int(input())
    a = list(map(int, input().split()))
    # a = [1, 4, 1, 2, 2, 1]
    # a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    a.sort()
    # print(a)
    # print(len(a))
    count = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()