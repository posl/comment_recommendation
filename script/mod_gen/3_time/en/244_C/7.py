def main():
    n = int(input())
    a = [0] * (2 * n + 1)
    a[0] = 1
    a[2 * n] = 1
    for i in range(2 * n):
        print(i + 1)
        a[i] = 1
        b = int(input())
        if b == 0:
            return
        a[b - 1] = 1
    print(0)
main()

if __name__ == '__main__':
    main()