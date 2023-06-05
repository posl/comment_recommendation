def main():
    n = int(input())
    x = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += abs(x[i])
    print(sum)
    sum = 0
    for i in range(n):
        sum += x[i]*x[i]
    print(sum**0.5)
    max = 0
    for i in range(n):
        if max < abs(x[i]):
            max = abs(x[i])
    print(max)

if __name__ == '__main__':
    main()