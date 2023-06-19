def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += 1 / a[i]
    print(1 / result)

if __name__ == '__main__':
    main()