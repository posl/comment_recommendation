def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    a_sum = sum(a)
    loop = x // a_sum
    x -= a_sum * loop
    ans = n * loop
    for i in range(n):
        if x < 0:
            break
        x -= a[i]
        ans += 1
    print(ans)
