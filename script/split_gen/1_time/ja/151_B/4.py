def main():
    n,k,m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = n*m - sum(a)
    if ans < 0:
        ans = 0
    elif ans > k:
        ans = -1
    print(ans)
