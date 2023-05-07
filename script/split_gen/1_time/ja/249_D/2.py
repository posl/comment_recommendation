def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += (a[i] * a[j]) // a[i]
    print(ans)
