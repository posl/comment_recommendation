def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum(a))
    else:
        print(sum(a[1:]) - a[0] * 2)

if __name__ == '__main__':
    main()