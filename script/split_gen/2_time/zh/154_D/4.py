def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(n, k, p)
    sum_p = sum(p[0:k])
    max_sum_p = sum_p
    for i in range(k, n):
        sum_p = sum_p + p[i] - p[i-k]
        if sum_p > max_sum_p:
            max_sum_p = sum_p
    print((max_sum_p + k) / 2)
