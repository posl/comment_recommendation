def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    minus = 0
    min_minus = 10**9
    for i in range(n):
        if a[i] < 0:
            minus += 1
            a[i] *= -1
        if a[i] < min_minus:
            min_minus = a[i]
        ans += a[i]
    if minus%2 == 0:
        print(ans)
    else:
        print(ans - min_minus*2)
