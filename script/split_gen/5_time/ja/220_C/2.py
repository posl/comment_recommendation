def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    cnt = 0
    if x > sum_a:
        cnt = n * (x // sum_a)
        x = x % sum_a
    sum_b = 0
    for i in range(n):
        sum_b += a[i]
        cnt += 1
        if sum_b > x:
            break
    print(cnt)
