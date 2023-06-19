def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(k):
        sum += p[i]
    max = sum
    for i in range(k, n):
        sum += p[i] - p[i-k]
        if sum > max:
            max = sum
    print((max+k)/2)

if __name__ == '__main__':
    main()