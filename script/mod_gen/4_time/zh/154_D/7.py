def main():
    n, k = map(int, input().split())
    pl = list(map(int, input().split()))
    p_sum = sum(pl[:k])
    max_p_sum = p_sum
    for i in range(k, n):
        p_sum += pl[i] - pl[i-k]
        if p_sum > max_p_sum:
            max_p_sum = p_sum
    print((max_p_sum + k) / 2)

if __name__ == '__main__':
    main()