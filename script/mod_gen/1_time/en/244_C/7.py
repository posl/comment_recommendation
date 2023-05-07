def main():
    n = int(input())
    a = [0] * (2 * n + 1)
    for i in range(n):
        a[i] = 1
        a[2 * n - i] = 1
        print(i + 1)
        a[int(input()) - 1] = 1
        print(2 * n - i + 1)
        a[int(input()) - 1] = 1
        for j in range(2 * n + 1):
            if a[j] == 0:
                print(j + 1)
                a[int(input()) - 1] = 1
                break
main()

if __name__ == '__main__':
    main()