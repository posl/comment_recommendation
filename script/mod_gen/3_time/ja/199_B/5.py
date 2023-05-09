def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(1, 1001):
        for j in range(n):
            if a[j] <= i <= b[j]:
                if j == n - 1:
                    count += 1
            else:
                break
    print(count)

if __name__ == '__main__':
    main()