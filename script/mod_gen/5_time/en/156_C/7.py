def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    min = 100000000000000
    for i in range(x[0], x[n-1]+1):
        sum = 0
        for j in range(n):
            sum += (x[j] - i)**2
        if min > sum:
            min = sum
    print(min)

if __name__ == '__main__':
    main()