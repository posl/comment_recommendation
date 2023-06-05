def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(1, a[j] + 1):
                if max < k * (j - i + 1):
                    max = k * (j - i + 1)
    print(max)
    return

if __name__ == '__main__':
    main()