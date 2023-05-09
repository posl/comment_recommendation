def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    count = x // sum_a
    x = x % sum_a
    sum_a = 0
    for i in range(n):
        sum_a += a[i]
        count += 1
        if sum_a > x:
            break
    print(count)
