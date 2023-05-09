def main():
    a, n = map(int, input().split())
    if a == 1:
        print(n-1)
        return
    x = 1
    for i in range(1, n+1):
        x = x * a
        if x > n:
            print(i-1)
            return
main()

if __name__ == '__main__':
    main()