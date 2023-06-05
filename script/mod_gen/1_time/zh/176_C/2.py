def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = 0
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            b[i + 1] = b[i] + 1
        else:
            b[i + 1] = b[i]
    print(b[n - 1])

if __name__ == '__main__':
    main()