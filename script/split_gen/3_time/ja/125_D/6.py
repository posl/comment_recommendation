def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    neg = 0
    min_abs = 10**9
    for i in range(n):
        if a[i] < 0:
            neg += 1
        ans += abs(a[i])
        min_abs = min(min_abs, abs(a[i]))
    if neg % 2 == 0:
        print(ans)
    else:
        print(ans - min_abs*2)
