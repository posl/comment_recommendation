def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = [0] * n
    x[0] = (a[0] + a[-1] - a[1]) // 2
    for i in range(1, n):
        x[i] = a[i - 1] - x[i - 1]
    print(" ".join(map(str, x)))

if __name__ == '__main__':
    main()