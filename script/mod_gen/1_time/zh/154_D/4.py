def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    sum_p = sum(p[:k])
    max_sum_p = sum_p
    for i in range(k,n):
        sum_p = sum_p - p[i-k] + p[i]
        if sum_p > max_sum_p:
            max_sum_p = sum_p
    print((max_sum_p+k)/2)

if __name__ == '__main__':
    main()