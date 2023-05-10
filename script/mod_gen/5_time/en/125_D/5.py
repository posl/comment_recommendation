def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] < 0:
        if n % 2 == 0:
            print(sum(map(abs, a)))
        else:
            print(sum(map(abs, a)) - 2*abs(a[0]))
    else:
        print(sum(a))

if __name__ == '__main__':
    main()