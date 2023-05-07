def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    ans = 0
    for i in range(n-1):
        ans += abs(a[i]-a[i+1])
    for i in range(q):
        if i == 0:
            print(ans + abs(a[0]-x[i]) + abs(a[1]-x[i]))
        elif i == q-1:
            print(ans + abs(a[n-2]-x[i]) + abs(a[n-1]-x[i]))
        else:
            print(ans + abs(a[i-1]-x[i]) + abs(a[i+1]-x[i]) - abs(a[i-1]-a[i]) - abs(a[i]-a[i+1]))
        a[i] = x[i]
