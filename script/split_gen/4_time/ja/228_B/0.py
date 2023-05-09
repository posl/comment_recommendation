def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    ans = 1
    for i in range(n):
        if a[i] != 0:
            ans += 1
            a[a[i]-1] = 0
    print(ans)
