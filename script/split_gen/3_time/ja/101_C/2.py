def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-k+1):
        if a[i] != ans:
            ans += 1
        else:
            ans = 1
    print(ans)
