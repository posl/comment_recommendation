def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] - (i+1)
    sum = abs(sum)
    print(sum)

if __name__ == '__main__':
    main()