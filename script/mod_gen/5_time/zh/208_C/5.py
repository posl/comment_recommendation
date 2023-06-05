def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    num = k // n
    mod = k % n
    for i in range(n):
        if i < mod:
            print(num + 1)
        else:
            print(num)

if __name__ == '__main__':
    main()