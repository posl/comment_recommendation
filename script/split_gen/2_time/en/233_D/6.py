def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        sum_a = 0
        for j in range(i, n):
            sum_a += a[j]
            if sum_a == k:
                cnt += 1
    print(cnt)
