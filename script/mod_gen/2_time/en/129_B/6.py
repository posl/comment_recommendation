def main():
    n = int(input())
    weights = list(map(int, input().split()))
    sum1 = sum(weights)
    sum2 = 0
    min_diff = sum1
    for i in range(n-1):
        sum1 -= weights[i]
        sum2 += weights[i]
        diff = abs(sum1-sum2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()