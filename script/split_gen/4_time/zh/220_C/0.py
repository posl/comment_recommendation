def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    s = sum(a)
    k = x // s
    ans = n * k
    x -= s * k
    for i in range(n):
        x -= a[i]
        ans += 1
        if x < 0:
            break
    print(ans)
