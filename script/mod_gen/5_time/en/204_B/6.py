def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    total = 0
    for i in range(n):
        if a[i] > 10:
            total += a[i] - 10
    print(total)

if __name__ == '__main__':
    main()