def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0 and (a[i] % 3 != 0 and a[i] % 5 != 0):
            print('DENIED')
            return
    print('APPROVED')

if __name__ == '__main__':
    main()