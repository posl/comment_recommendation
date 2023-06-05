def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    sum = 0
    for i in range(k):
        sum += p[i]
    max = sum
    for i in range(k, n):
        sum = sum - p[i-k] + p[i]
        if sum > max:
            max = sum
    print((max + k)/2)
