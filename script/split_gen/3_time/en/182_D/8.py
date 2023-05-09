def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if a[i] <= 0:
            ans += -a[i]
        else:
            ans += a[i]
    print(ans)
