def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        if n % a[i] == 0:
            print(n)
            return
    for i in range(k):
        if n % a[i] != 0:
            print(n - n % a[i])
            return
main()

if __name__ == '__main__':
    main()