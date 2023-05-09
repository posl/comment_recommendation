def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += max(a[i]-k*x,0)
    print(ans)
