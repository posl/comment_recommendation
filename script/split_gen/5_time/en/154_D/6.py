def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    max_sum = 0
    for i in range(k):
        max_sum += (p[i] + 1) / 2
    temp_sum = max_sum
    for i in range(k, n):
        temp_sum = temp_sum - (p[i - k] + 1) / 2 + (p[i] + 1) / 2
        if temp_sum > max_sum:
            max_sum = temp_sum
    print(max_sum)
