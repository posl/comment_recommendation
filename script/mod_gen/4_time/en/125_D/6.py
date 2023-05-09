def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum(a))
    else:
        print(sum(a) - 2 * a[0])

if __name__ == '__main__':
    main()