def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += b[a[i] - 1]
        if i < n - 1 and a[i + 1] == a[i] + 1:
            result += c[a[i] - 1]
    print(result)

if __name__ == '__main__':
    main()