def main():
    n = int(input())
    w = list(map(int, input().split()))
    min_diff = 1000000
    for t in range(1, n):
        sum1 = sum(w[:t])
        sum2 = sum(w[t:])
        diff = abs(sum1 - sum2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()