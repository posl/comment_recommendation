def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    max_sum = 0
    for i in range(n-k+1):
        s = sum(a[i:i+k])
        if s % d == 0:
            max_sum = max(max_sum, s)
    if max_sum == 0:
        print(-1)
    else:
        print(max_sum)
