def main():
    N = int(input())
    a = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 1:
                print(count)
                return
            a[i] //= 2
        count += 1
main()

if __name__ == '__main__':
    main()