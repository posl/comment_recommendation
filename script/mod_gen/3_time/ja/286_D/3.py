def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += a[j] * b[j]
        if sum == x:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()