def main():
    n = int(input())
    x = list(map(int, input().split()))
    min = 100000000
    for i in range(1, 101):
        sum = 0
        for j in range(n):
            sum += (x[j] - i) ** 2
        if sum < min:
            min = sum
    print(min)

if __name__ == '__main__':
    main()