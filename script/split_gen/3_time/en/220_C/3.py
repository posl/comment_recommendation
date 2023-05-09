def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    s = sum(a)
    m = x // s
    ans = n * m
    x -= s * m
    for i in range(n):
        x -= a[i]
        ans += 1
        if x < 0:
            print(ans)
            exit()
