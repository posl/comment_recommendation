def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    x = int(input())
    sum_a = sum(a)
    sum_b = sum_a * (x // sum_a)
    ans = n * (x // sum_a)
    for i in range(n):
        sum_b += a[i]
        ans += 1
        if sum_b > x:
            break
    print(ans)
