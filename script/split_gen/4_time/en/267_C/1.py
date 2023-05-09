def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0]
    for i in range(n):
        sum_a.append(sum_a[i] + a[i])
    max_sum = -float('inf')
    for i in range(n-m+1):
        max_sum = max(max_sum, sum_a[i+m] - sum_a[i])
    print(max_sum)
