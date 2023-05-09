def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    if n == 2:
        print(ans)
        return
    for i in range(1, n-1):
        ans = max(ans, sum(a) - 2*sum(a[1:i+1:2]))
    print(ans)
