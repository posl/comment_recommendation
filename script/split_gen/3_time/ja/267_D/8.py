def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans, sum([(j+1)*a[i+j] for j in range(m)]))
    print(ans)
