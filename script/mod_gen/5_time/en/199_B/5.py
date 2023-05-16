def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(1, 1001):
        if all([a[j] <= i <= b[j] for j in range(n)]):
            count += 1
    print(count)

if __name__ == '__main__':
    main()