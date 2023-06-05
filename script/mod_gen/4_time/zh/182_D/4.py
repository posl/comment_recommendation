def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > max:
            max = sum
    print(max)

if __name__ == '__main__':
    main()