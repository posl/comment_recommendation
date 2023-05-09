def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if a[i] == count:
            count += 1
        elif a[i] > count:
            break
    print(count)

if __name__ == '__main__':
    main()