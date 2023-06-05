def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max = 0
    for i in range(k+1):
        sum = 0
        for j in range(n):
            sum += (i^a[j])
        if max < sum:
            max = sum
    print(max)

if __name__ == '__main__':
    main()