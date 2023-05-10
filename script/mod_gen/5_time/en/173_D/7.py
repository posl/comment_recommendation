def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    total = 0
    for i in range(2, n):
        total += a[i // 2]
    print(total)

if __name__ == '__main__':
    main()