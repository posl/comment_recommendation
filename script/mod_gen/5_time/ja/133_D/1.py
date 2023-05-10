def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = [0] * n
    for i in range(n):
        result[i] = a[i] - (a[i] // 2) * 2
    for i in range(n):
        if i == n - 1:
            print(result[i] + result[0])
        else:
            print(result[i] + result[i + 1])

if __name__ == '__main__':
    main()