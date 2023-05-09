def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            sum += a[i] - 1
        else:
            sum += a[i]
    if x >= sum:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()