def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p_sum = sum(p[:k])
    max_p_sum = p_sum
    for i in range(n-k):
        p_sum = p_sum - p[i] + p[i+k]
        if p_sum > max_p_sum:
            max_p_sum = p_sum
    print((max_p_sum+k)/2)

if __name__ == '__main__':
    main()