def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            continue
        else:
            ans += a[i-1] - a[i] + 1
            a[i] = a[i-1] + 1
    print(ans)
