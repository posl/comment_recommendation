def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += a[i] - 1
        else:
            if a[i] > a[i - 1]:
                ans += a[i] - a[i - 1] - 1
            elif a[i] == a[i - 1]:
                ans += a[i] - 1
            else:
                ans += a[i] - 1
    print(ans)
