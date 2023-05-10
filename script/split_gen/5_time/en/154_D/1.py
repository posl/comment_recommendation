def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    sum_p = [0] * (n+1)
    for i in range(n):
        sum_p[i+1] = sum_p[i] + p[i]
    max = 0
    for i in range(n-k+1):
        if max < sum_p[i+k] - sum_p[i]:
            max = sum_p[i+k] - sum_p[i]
    print((max + k) / 2)
main()
