def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p_max = sum(p[:k])
    p_sum = p_max
    for i in range(n-k):
        p_sum = p_sum - p[i] + p[i+k]
        if p_sum > p_max:
            p_max = p_sum
    print((p_max+k)/2)

if __name__ == '__main__':
    main()